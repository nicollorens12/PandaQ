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
            # Iterar sobre cada elemento selectItem y aplicar la lógica individualmente
            if ctx.selectItem():
                return self.visitSelectItem(ctx.selectItem(0), df)  # Actualizamos result_df con el único selectItem
            else:
                print(f"Error: No existe este selectItem.")
                return pd.DataFrame()
 
        else:
            print(f"Error: La tabla '{table_name}' no existe.")
            return pd.DataFrame()
  

    def visitSelectItem(self, ctx: lcParser.SelectItemContext, df):
        result_df = None
        if ctx.STAR():
            return df
        
        elif ctx.columnNameList():

            # Obtener la lista de columnas
            column_names = [col.getText() for col in ctx.columnNameList().columnName()]

            # Verificar si todas las columnas existen en el DataFrame
            missing_columns = [col for col in column_names if col not in df.columns]
            if missing_columns:
                print(f"Error: Las siguientes columnas no existen en el DataFrame: {', '.join(missing_columns)}")
                return df  # Devolvemos el DataFrame original

            # Realizar la lógica para actualizar el DataFrame según la lista de columnas
            result_df = df[column_names]

            return result_df  # Devolvemos el DataFrame actualizado
        
        elif ctx.expression(): #DEVUELVE UNA COLUMNA CALCULADA
            # Si hay una expresión, evaluarla y devolver el resultado
            series = self.visitExpression(ctx.expression(),df)
            print("DF ORIGINAL COLUMN: ",df.columns[0])
            print("NUEVO NOMBRE: ",ctx.columnName().getText())
            df = series.to_frame()
            print(df.columns[0])
            df.rename(ctx.columnName().getText())
            #print(df.name)
            return pd.concat([result_df, df], ignore_index=True)

        else:
            # Si no hay expresión ni columna, devolver None
            print("Error: selectItem no contiene una expresión, una columna ni una lista de columnas.")
            return None


    def visitExpression(self, ctx: lcParser.ExpressionContext,df): # TIENE QUE DEVOLVER LA COLUMNA NUEVA
        if ctx.PLUS():
            print("SUMMA ES:", ctx.expression(0), " ", ctx.expression(1))
            return self.visit(ctx.expression(0)) + self.visit(ctx.expression(1))
        elif ctx.MINUS():
            print("RESTA ES:", ctx.expression(0), " ", ctx.expression(1))
            return self.visit(ctx.expression(0)) - self.visit(ctx.expression(1))
        elif ctx.STAR():
            print("MULYIPLICACIN ES:", ctx.expression(0), " ", ctx.expression(1))
            return self.visit(ctx.expression(0)) * self.visit(ctx.expression(1))
        elif ctx.DIV():
            print("DIVISION ES:", ctx.expression(0), " ", ctx.expression(1))
            return self.visit(ctx.expression(0)) / self.visit(ctx.expression(1))
        elif ctx.LPAREN() and ctx.RPAREN():
            return self.visit(ctx.expression(0))
        elif ctx.columnName():
            # Manejar identificadores (columnas)
            column_name = ctx.columnName().getText()
            print("EL COLUM NAME ES: ", column_name) #es erroneo, da el column name antiguo
            return df[column_name]
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