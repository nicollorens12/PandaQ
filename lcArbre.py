from antlr4 import *
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
        order_by_expression_list = ctx.orderByExpressionList()

        if order_by_expression_list:
            print("HOLA")
            order_columns = [self.visitOrderByExpression(expr) for expr in order_by_expression_list.orderByExpression()]
            self.resultado = self.visitWithOrderBy(ctx.statement(), order_columns)
        elif ctx.statement():  # Asegúrate de que ctx.statement() no sea None
            self.resultado = self.visit(ctx.statement())
            
        else:
            print("No hay ORDER BY ni statement.")

            
    def visitWithOrderBy(self, ctx: lcParser.StatementContext, order_columns):
        result_df = self.visitStatement(ctx)
        print(order_columns)
        # Extraer los nombres de las columnas y las direcciones de ordenamiento
        order_columns_list = [order.split(" ") for order in order_columns]
        
        # Extraer solo los nombres de las columnas para pasar a sort_values
        column_names = [col[0] for col in order_columns_list]

        # Extraer las direcciones de ordenamiento o establecer ASC por defecto
        directions = [col[1].upper() if len(col) > 1 else 'ASC' for col in order_columns_list]
        
        # Ordenar el DataFrame según las columnas y direcciones especificadas
        if not result_df.empty:
            result_df.sort_values(by=column_names, ascending=[dir == 'ASC' for dir in directions], inplace=True)

        return result_df




    def visitStatement(self, ctx: lcParser.StatementContext):
        table_name = ctx.tableName().getText()
        select_items = ctx.selectItem() if ctx.selectItem() else []
        df = self.dataframes.get(table_name)
        print("BUENAS")
        if df is not None:
            result_df = pd.DataFrame()

            # Iterar sobre cada elemento selectItem y aplicar la logica individualmente
            for select_item in select_items:
                print("EII")
                select_item_result = self.visitSelectItem(select_item, df)
                result_df = pd.concat([result_df, select_item_result], axis=1)

            return result_df

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
                return pd.DataFrame()  # Devolvemos un DataFrame vacío

            # Realizar la lógica para actualizar el DataFrame según la lista de columnas
            result_df = df[column_names]

        elif ctx.expression():
            # Si hay una expresión, evaluarla y devolver el resultado
            result_df = self.visitExpression(ctx.expression(), df)
            #result_df = series.to_frame()
            result_df.rename(columns={result_df.columns[0]: ctx.columnName().getText()}, inplace=True)

        else:
            # Si no hay expresión ni columna, devolver None
            print("Error: selectItem no contiene una expresión, una columna ni una lista de columnas.")
            return None

        return result_df

    def visitExpression(self, ctx: lcParser.ExpressionContext, df):  # TIENE QUE DEVOLVER LA COLUMNA NUEVA
        if ctx.PLUS() or ctx.MINUS() or ctx.STAR() or ctx.DIV():
            column_name = ctx.expression(0).getText()
            value = self.visitExpression(ctx.expression(1), df)

            if ctx.PLUS():
                df[column_name] = df[column_name] + value
            elif ctx.MINUS():
                df[column_name] = df[column_name] - value
            elif ctx.STAR():
                df[column_name] = df[column_name] * value
            elif ctx.DIV():
                df[column_name] = df[column_name] / value

            nuevo_df = df[[column_name]].copy()
            return nuevo_df

        elif ctx.columnName():
            # Manejar identificadores (columnas)
            column_name = ctx.columnName().getText()
            return df[column_name].to_frame()

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

    def visitOrderByExpressionList(self, ctx: lcParser.OrderByExpressionListContext):
        return [self.visit(expr) for expr in ctx.orderByExpression()]

    def visitOrderByExpression(self, ctx: lcParser.OrderByExpressionContext):
        column_name = self.visitColumnName(ctx.columnName())
        
        # Verificar si hay ASC o DESC
        if ctx.ASC():
            direction = "ASC"
        elif ctx.DESC():
            direction = "DESC"
        else:
            direction = "ASC"  # Si no se especifica, asumir ASC
        
        return f"{column_name} {direction}"


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
