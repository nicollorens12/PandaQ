# Generated from pandaQ.g4 by ANTLR 4.13.1
from antlr4 import *
import pandas as pd

if "." in __name__:
    from .pandaQParser import pandaQParser
else:
    from pandaQParser import pandaQParser

# This class defines a complete generic visitor for a parse tree produced by pandaQParser.

class pandaQVisitor(ParseTreeVisitor):
    def __init__(self, dataframes):
        self.dataframes = dataframes
        self.resultado = None

    # Visit a parse tree produced by pandaQParser#instruction.
    def visitInstruction(self, ctx:pandaQParser.InstructionContext):
        self.visitChildren(ctx)

    # Visit a parse tree produced by pandaQParser#plot.
    def visitPlot(self, ctx:pandaQParser.PlotContext):
        table_name = ctx.tableName().getText()
        self.instruction_type = "plot"
        original_df = self.dataframes.get(table_name, pd.DataFrame())

        # Filtrar solo las columnas numericas ya que son las que se hace el plot
        numeric_columns_df = original_df.select_dtypes(include='number')
        self.resultado = numeric_columns_df



    # Visit a parse tree produced by pandaQParser#assignment.
    def visitAssignment(self, ctx:pandaQParser.AssignmentContext):
        variable_name = ctx.ID().getText()
        self.visitQuery(ctx.query())

        self.dataframes[variable_name] = self.resultado


    # Visit a parse tree produced by pandaQParser#query.
    def visitQuery(self, ctx:pandaQParser.QueryContext):
        self.resultado = self.visit(ctx.statement())
        
        if ctx.orderByExpressionList():
            order_columns = self.visitOrderByExpressionList()
            self.resultado = self.visitWithOrderBy(ctx.statement(), order_columns)


    # Visit a parse tree produced by pandaQParser#statement.
    def visitStatement(self, ctx:pandaQParser.StatementContext):
        select_items = ctx.selectItem() if ctx.selectItem() else []
        df = self.visitTableSource(ctx.tableSource())
        if df is not None:
            result_df = pd.DataFrame()

            # Filtrar el DataFrame según la condición WHERE si está presente
            if ctx.condition():
                df = self.visitChildren(ctx)

            # Iterar sobre cada elemento selectItem y aplicar la lógica individualmente
            for select_item in select_items:
                select_item_result = self.visitSelectItem(select_item, df)
                result_df = pd.concat([result_df, select_item_result], axis=1)

            return result_df

        else:
            print(f"Error: La tabla esta vacia.")
            return pd.DataFrame()

    # Visit a parse tree produced by pandaQParser#all.
    def visitAll(self, ctx:pandaQParser.AllContext,df):
        return df

    def visitSelection(self, ctx:pandaQParser.SelectionContext,df):
        return df

    # Visit a parse tree produced by pandaQParser#selectItemColumnNameList.
    def visitSelectItemColumnName(self, ctx:pandaQParser.SelectItemColumnName,df):
        # Obtener la lista de columnas
        column_names = [col.getText() for col in ctx.columnNameList().columnName()]

        # Verificar si todas las columnas existen en el DataFrame
        missing_columns = [col for col in column_names if col not in df.columns]
        if missing_columns:
            print(f"Error: Las siguientes columnas no existen en el DataFrame: {', '.join(missing_columns)}")
            return pd.DataFrame()  # Devolvemos un DataFrame vacío

        return df[column_names]


    # Visit a parse tree produced by pandaQParser#selectItemAS.
    def visitSelectItemAS(self, ctx:pandaQParser.SelectItemASContext,df):
        # Si hay una expresión, evaluarla y devolver el resultado
        result_df = self.visitExpression(ctx.expression(), df)
        result_df.rename(columns={result_df.columns[0]: ctx.columnName().getText()}, inplace=True)


    # Visit a parse tree produced by pandaQParser#expressionNumber.
    def visitExpressionNumber(self, ctx:pandaQParser.ExpressionNumberContext):
        return float(ctx.NUMBER().getText())


    # Visit a parse tree produced by pandaQParser#expressionAritmetic.
    def visitExpressionAritmetic(self, ctx:pandaQParser.ExpressionAritmeticContext,df):
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


    # Visit a parse tree produced by pandaQParser#expressionColumnName.
    def visitExpressionColumnName(self, ctx:pandaQParser.ExpressionColumnNameContext,df):
        column_name = ctx.columnName().getText()
        return df[column_name].to_frame()


    # Visit a parse tree produced by pandaQParser#columnNameList.
    def visitColumnNameList(self, ctx:pandaQParser.ColumnNameListContext):
        return [self.visit(column_name) for column_name in ctx.columnName()]


    # Visit a parse tree produced by pandaQParser#columnName.
    def visitColumnName(self, ctx:pandaQParser.ColumnNameContext):
        return ctx.ID().getText()


    # Visit a parse tree produced by pandaQParser#tableSource.
    def visitTableSource(self, ctx:pandaQParser.TableSourceContext):
        num_tables = len(ctx.tableName())

        if num_tables == 1:
            # Si solo hay una tabla y no hay INNER JOIN, devolver el DataFrame correspondiente
            return self.dataframes.get(ctx.tableName(0).getText(), pd.DataFrame())
        elif ctx.INNER() and ctx.JOIN() and ctx.ON() and ctx.condition():
            # Si hay al menos un INNER JOIN, aplicar la condición ON
            # Inicializar el DataFrame con la primera tabla
            result_df = self.dataframes.get(ctx.tableName(0).getText(), pd.DataFrame())

            # Iterar sobre las tablas y condiciones INNER JOIN
            for i in range(1, num_tables):
                right_df = self.dataframes.get(ctx.tableName(i).getText(), pd.DataFrame())
                condition_result = self.visitCondition(ctx.condition(i - 1), pd.DataFrame())  # La condición ON se evalúa con un DataFrame vacío
                result_df = pd.merge(result_df, right_df, how='inner', left_on=condition_result[0], right_on=condition_result[1])

            return result_df
        else:
            print("Error: No se pudo determinar la fuente de la tabla.")
            return pd.DataFrame()

    # Visit a parse tree produced by pandaQParser#tableName.
    def visitTableName(self, ctx:pandaQParser.TableNameContext):
        return ctx.ID().getText()


    # Visit a parse tree produced by pandaQParser#orderByExpressionList.
    def visitOrderByExpressionList(self, ctx:pandaQParser.OrderByExpressionListContext):
        order_columns = [self.visit(expr) for expr in ctx.orderByExpression()]
        
        result_df = self.visitStatement(ctx)
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


    # Visit a parse tree produced by pandaQParser#orderByExpression.
    def visitOrderByExpression(self, ctx:pandaQParser.OrderByExpressionContext):
        column_name = self.visitColumnName(ctx.columnName())
        
        if ctx.DESC():
            direction = "DESC"
        else:
            direction = "ASC"  # En cualquier otro caso, ASC
        
        return f"{column_name} {direction}"


    # Visit a parse tree produced by pandaQParser#conditionBoolean.
    def visitConditionBoolean(self, ctx:pandaQParser.ConditionBooleanContext,df):
        return self.visitBooleanExpression(ctx.booleanExpression(), df)


    # Visit a parse tree produced by pandaQParser#conditionEqual.
    def visitConditionEqual(self, ctx:pandaQParser.ConditionEqualContext,df):
        column_name1 = self.visitColumnName(ctx.columnName(0))
        column_name2 = self.visitColumnName(ctx.columnName(1))
        return df[column_name1, column_name2]


    # Visit a parse tree produced by pandaQParser#conditionIn.
    def visitConditionIn(self, ctx:pandaQParser.ConditionInContext,df):
        column_name = self.visitColumnName(ctx.columnName())
        subquery_result = self.visit(ctx.query())

        if not subquery_result.empty:
            # Verificar si la columna en la que estamos aplicando el IN existe en el DataFrame del subquery
            if column_name not in subquery_result.columns:
                print(f"Error: La columna '{column_name}' no existe en el subquery.")
                return pd.DataFrame()

            # Filtrar el DataFrame original para aquellos valores que están en el subquery
            return df[df[column_name].isin(subquery_result[column_name])]

        return pd.DataFrame()


    # Visit a parse tree produced by pandaQParser#booleanExpression.
    def visitBooleanExpression(self, ctx:pandaQParser.BooleanExpressionContext,df):
        boolean_term_results = [self.visitBooleanTerm(term, df) for term in ctx.booleanTerm()]
        if ctx.OR():
            return boolean_term_results[0] | boolean_term_results[1]
        else:
            return boolean_term_results[0]


    # Visit a parse tree produced by pandaQParser#booleanTerm.
    def visitBooleanTerm(self, ctx:pandaQParser.BooleanTermContext):
        boolean_factor_results = [self.visitBooleanFactor(factor, df) for factor in ctx.booleanFactor()]
        if ctx.AND():
            return boolean_factor_results[0] & boolean_factor_results[1]
        else:
            return boolean_factor_results[0]


    # Visit a parse tree produced by pandaQParser#booleanFactor.
    def visitBooleanFactor(self, ctx:pandaQParser.BooleanFactorContext,df):
        boolean_primary_result = self.visit(ctx.getChildren(), df)
        if ctx.NOT():
            return ~boolean_primary_result
        else:
            return boolean_primary_result


    # Visit a parse tree produced by pandaQParser#booleanPrimaryBoolean.
    def visitBooleanPrimaryBoolean(self, ctx:pandaQParser.BooleanPrimaryBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#booleanPrimaryComparison.
    def visitBooleanPrimaryComparison(self, ctx:pandaQParser.BooleanPrimaryComparisonContext,df):
        return self.visitChildren(ctx,df)
       

    # Visit a parse tree produced by pandaQParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:pandaQParser.ComparisonExpressionContext,df):

        # Obtener el nombre de la columna (primer operando)
        column_name = self.visitColumnName(ctx.columnName())
        column_name2 = ctx.columnName().getText()

        # Obtener la expresión constante (segundo operando)
        constant_operand = None
        if ctx.NUMBER():
            constant_operand = float(ctx.NUMBER().getText())
        elif ctx.TRUE():
            constant_operand = True
        elif ctx.FALSE():
            constant_operand = False
        elif ctx.STRING():
            constant_operand = ctx.STRING().getText()[1:-1]  # Eliminar comillas de inicio y fin
    
        # Obtener los valores reales de la columna y la expresión constante
        left_operand = df[column_name] if column_name in df.columns else None
        right_operand = constant_operand

    
        if left_operand is not None:
            # Realizar la comparación según el operador
            if ctx.EQUAL():
                return left_operand == right_operand
            elif ctx.NOT_EQUAL():
                return left_operand != right_operand
            elif ctx.LESS():
                return left_operand < right_operand
            elif ctx.LESS_OR_EQUAL():
                return left_operand <= right_operand
            elif ctx.GREATER():
                return left_operand > right_operand
            elif ctx.GREATER_OR_EQUAL():
                return left_operand >= right_operand
            else:
                return None
        else:
            print(f"Error: La columna '{column_name}' no existe en el DataFrame.")
            return None

    def filterDataFrame(self, df, condition):
        condition_result = self.visitCondition(condition, df)
        return df[condition_result]



del pandaQParser