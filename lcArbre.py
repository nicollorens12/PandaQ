from antlr4 import *
if "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser
import pandas as pd

if "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser

class lcArbre(ParseTreeVisitor):
    def __init__(self, dataframes):
        self.dataframes = dataframes
        self.resultado = None

    def visitQuery(self, ctx: lcParser.QueryContext):
        self.resultado = self.visit(ctx.statement())

    def visitStatement(self, ctx: lcParser.StatementContext):
        table_name = ctx.tableName().getText()
        select_items = ctx.selectItem() if ctx.selectItem() else []
        df = self.dataframes.get(table_name)
        print('FLAG 0')
        if df is not None:
            # Verificar si hay al menos '*' en la lista de select_items
            if any(item.getText() == '*' for item in select_items):
                print('FLAG 1')
                # Si hay '*', devolver todo el DataFrame
                result_df = df
            else:
                print('FLAG 2')
                # Filtrar los nombres de las columnas que no son nulos
                column_names = [self.visit(item) for item in select_items if self.visit(item) is not None]
                result_df = df[column_names]
            return result_df
        else:
            print(f"Error: La tabla '{table_name}' no existe.")
            return pd.DataFrame()


        
    def visitSelectItem(self, ctx: lcParser.SelectItemContext):
        if ctx.expression():
            # Si hay una expresión, evaluarla y mostrar el resultado
            expression_result = self.visit(ctx.expression())
            print(expression_result)
        elif ctx.columnName():
            # Si hay una columna, imprimir su nombre
            print(ctx.columnName().getText())
        else:
            print("Error: selectItem no contiene una expresión ni una columna.")


    def visitExpression(self, ctx: lcParser.ExpressionContext):
        if ctx.PLUS():
            return self.visit(ctx.expression(0)) + self.visit(ctx.expression(1))
        elif ctx.MINUS():
            return self.visit(ctx.expression(0)) - self.visit(ctx.expression(1))
        elif ctx.STAR():
            return self.visit(ctx.expression(0)) * self.visit(ctx.expression(1))
        elif ctx.DIV():
            return self.visit(ctx.expression(0)) / self.visit(ctx.expression(1))
        elif ctx.LPAREN() and ctx.RPAREN():
            return self.visit(ctx.expression(0))
        elif ctx.ID():
            # Manejar identificadores (columnas)
            column_name = ctx.ID().getText()
            # En lugar de devolver un DataFrame, simplemente imprimir el nombre de la columna
            print(column_name)
        elif ctx.INTEGER():
            # Manejar enteros
            return int(ctx.INTEGER().getText())
        else:
            print("Expresión no reconocida")
            return None

    def visitColumnNameList(self, ctx: lcParser.ColumnNameListContext):
        return [self.visit(column_name) for column_name in ctx.columnName()]

    def visitColumnName(self, ctx: lcParser.ColumnNameContext):
        return ctx.ID().getText()

    def visitTableName(self, ctx: lcParser.TableNameContext):
        return ctx.ID().getText()

    def printResult(self):
        if self.resultado is not None:
            print(self.resultado.to_string(index=False))
        else:
            print("No hay resultado para imprimir.")
    
    def get_result(self):
        return self.resultado