from antlr4 import *
import pandas as pd

if "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser

class QVisitor(ParseTreeVisitor):
    def __init__(self, dataframes):
        self.dataframes = dataframes
        self.resultado = None
        self.instruction_type = None 
    
    def visitInstruction(self, ctx: lcParser.InstructionContext):
        if ctx.plot():
            self.instruction_type = "plot"
            table_name = self.visitPlot(ctx.plot())
            original_df = self.dataframes.get(table_name, pd.DataFrame())

            # Filtrar solo las columnas numericas ya que son las que se hace el plot
            numeric_columns_df = original_df.select_dtypes(include='number')
            self.resultado = numeric_columns_df
        elif ctx.assignment():
            self.instruction_type = "assignment"
            self.visitAssignment(ctx.assignment())
        elif ctx.query():
            self.instruction_type = "query"
            self.visitQuery(ctx.query())
        
        else:
            print("Error: Instrucción no reconocida.")
    
    def visitPlot(self, ctx: lcParser.PlotContext):
        return ctx.tableName().getText()
    
    def visitAssignment(self, ctx: lcParser.AssignmentContext):
        variable_name = ctx.ID().getText()
        self.visitQuery(ctx.query())

        self.dataframes[variable_name] = self.resultado

    def visitQuery(self, ctx: lcParser.QueryContext):
        order_by_expression_list = ctx.orderByExpressionList()
        
        if order_by_expression_list:
            order_columns = [self.visitOrderByExpression(expr) for expr in order_by_expression_list.orderByExpression()]
            self.resultado = self.visitWithOrderBy(ctx.statement(), order_columns)
        elif ctx.statement():
            self.resultado = self.visit(ctx.statement())            
        else:
            print("No hay ORDER BY ni statement.")

    def visitStatement(self, ctx: lcParser.StatementContext):
        select_items = ctx.selectItem() if ctx.selectItem() else []
        df = self.visitTableSource(ctx.tableSource())
        if df is not None:
            result_df = pd.DataFrame()

            # Filtrar el DataFrame según la condición WHERE si está presente
            where_condition = ctx.condition()
            if where_condition:
                df = self.filterDataFrame(df, where_condition)

            # Iterar sobre cada elemento selectItem y aplicar la lógica individualmente
            for select_item in select_items:
                select_item_result = self.visitSelectItem(select_item, df)
                result_df = pd.concat([result_df, select_item_result], axis=1)

            return result_df

        else:
            print(f"Error: La tabla esta vacia.")
            return pd.DataFrame()

    def visitTableSource(self, ctx: lcParser.TableSourceContext):
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

    def visitCondition(self, ctx: lcParser.ConditionContext, df):
        if ctx.booleanExpression():
            print("WHERE NORMAL")

            # Si es una expresión booleana, evaluarla directamente
            return self.visitBooleanExpression(ctx.booleanExpression(), df)
        
        elif ctx.columnName(0) and ctx.columnName(1) and ctx.EQUAL():
            # Si es una comparación entre columnas, realizar la comparación
            column_name1 = self.visitColumnName(ctx.columnName(0))
            column_name2 = self.visitColumnName(ctx.columnName(1))
            return [column_name1, column_name2]
        
        elif ctx.columnName() and ctx.IN(): 
            self.visitQuery(ctx.query())
            subquery_df = self.resultado 
            column_name = self.visitColumnName(ctx.columnName(0)) 
    
            result_df = df[column_name].isin(subquery_df[column_name])
            return result_df
    
        else:
            print("Error: Condición no reconocida.")
            return None

    def filterDataFrame(self, df, condition):
        condition_result = self.visitCondition(condition, df) 
        return df[condition_result]

    def visitBooleanExpression(self, ctx: lcParser.BooleanExpressionContext, df):
        boolean_term_results = [self.visitBooleanTerm(term, df) for term in ctx.booleanTerm()]
        if ctx.OR():
            return boolean_term_results[0] | boolean_term_results[1]
        else:
            return boolean_term_results[0]

    def visitBooleanTerm(self, ctx: lcParser.BooleanTermContext, df):
        boolean_factor_results = [self.visitBooleanFactor(factor, df) for factor in ctx.booleanFactor()]
        if ctx.AND():
            return boolean_factor_results[0] & boolean_factor_results[1]
        else:
            return boolean_factor_results[0]

    def visitBooleanFactor(self, ctx: lcParser.BooleanFactorContext, df):
        boolean_primary_result = self.visitBooleanPrimary(ctx.booleanPrimary(), df)
        if ctx.NOT():
            return ~boolean_primary_result
        else:
            return boolean_primary_result

    def visitBooleanPrimary(self, ctx: lcParser.BooleanPrimaryContext, df):
        if ctx.comparisonExpression():
            return self.visitComparisonExpression(ctx.comparisonExpression(), df)
        else:
            return None

    def visitComparisonExpression(self, ctx: lcParser.ComparisonExpressionContext, df):
        # Obtener el nombre de la columna (primer operando)
        column_name = self.visitColumnName(ctx.columnName())

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
                return pd.DataFrame() 

            result_df = df[column_names]

        elif ctx.expression():
            result_df = self.visitExpression(ctx.expression(), df)
            result_df.rename(columns={result_df.columns[0]: ctx.columnName().getText()}, inplace=True)

        else:
            # Si no hay expresión ni columna, devolver None
            print("Error: selectItem no contiene una expresión, una columna ni una lista de columnas.")
            return None

        return result_df

    def visitExpression(self, ctx: lcParser.ExpressionContext, df):
        if ctx.PLUS() or ctx.MINUS() or ctx.STAR() or ctx.DIV():
            column_name = ctx.expression(0).getText()
            value = self.visitExpression(ctx.expression(1), df)

            if ctx.PLUS():
                df.loc[:, column_name] = df[column_name] + value
            elif ctx.MINUS():
                df.loc[:, column_name] = df[column_name] - value
            elif ctx.STAR():
                df.loc[:, column_name] = df[column_name] * value
            elif ctx.DIV():
                df.loc[:, column_name] = df[column_name] / value

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
    
    def visitWithOrderBy(self, ctx: lcParser.StatementContext, order_columns):
        result_df = self.visitStatement(ctx)
        order_columns_list = [order.split(" ") for order in order_columns]
        
        column_names = [col[0] for col in order_columns_list]

        directions = [col[1].upper() if len(col) > 1 else 'ASC' for col in order_columns_list]
        
        if not result_df.empty:
            result_df.sort_values(by=column_names, ascending=[dir == 'ASC' for dir in directions], inplace=True)

        return result_df

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

    def empty_instruction_type(self):
        self.instruction_type = None
    