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

        if df is not None:
            # Verificar si hay al menos '*' en la lista de select_items
            if any(self.isSelectAll(item) for item in select_items):
                # Si hay '*', devolver todo el DataFrame
                result_df = df
            else:
                # Filtrar los nombres de las columnas que no son nulos
                column_names = [name for item in select_items for name in self.visitSelectItem(item) if name is not None]
                print("column names retornado:", column_names)
                result_df = df[column_names]

            return result_df
        else:
            print(f"Error: La tabla '{table_name}' no existe.")
            return pd.DataFrame()
  

    def visitSelectItem(self, ctx: lcParser.SelectItemContext):

        if ctx.expression():
            # Si hay una expresión, evaluarla y devolver el resultado
            expression_result = self.visit(ctx.expression())
            #print("Expression result:", expression_result)
            return expression_result
        elif ctx.columnName():
            print("ENTRO")
            # Si hay una columna, devolver su nombre
            column_name = ctx.columnName().getText()
            #print("Column name:", column_name)
            return column_name
        elif ctx.columnNameList():
            print("ENTRO 2")
            # Si hay una lista de nombres de columna, procesarla según sea necesario
            column_names = [self.visit(column) for column in ctx.columnNameList().columnName()]
            print("Column names list:", column_names)
            return column_names
        else:
            # Si no hay expresión ni columna, devolver None
            print("Error: selectItem no contiene una expresión, una columna ni una lista de columnas.")
            return None


    def visitExpression(self, ctx: lcParser.ExpressionContext): # NO VA LA MULTIPLICACION
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
        elif ctx.columnName():
            # Manejar identificadores (columnas)
            column_name = ctx.columnName().getText()
            # En lugar de devolver un DataFrame, simplemente imprimir el nombre de la columna
            return column_name
        elif ctx.NUMBER():
            # Manejar enteros
            return float(ctx.NUMBER().getText())
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
    
    def isSelectAll(self, item: lcParser.SelectItemContext) -> bool:
        # Verificar si el item es '*' y si le sigue directamente un FROM en la lista de select_items
        if item.STAR() is not None:
            return True
        return False