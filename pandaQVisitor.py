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
        self.instruction_type = None
        self.source = pd.DataFrame() 
        self.resultado = pd.DataFrame()
        self.order_columns = []
        self.directions = []
        self.where = pd.DataFrame()
        
    # Visit a parse tree produced by pandaQParser#instruction.
    def visitInstruction(self, ctx:pandaQParser.InstructionContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#plot.
    def visitPlot(self, ctx:pandaQParser.PlotContext):
        self.instruction_type = "plot"
        original_df = self.dataframes.get(self.visitChildren(ctx), pd.DataFrame())
        self.resultado = original_df.select_dtypes(include='number')
        
    # Visit a parse tree produced by pandaQParser#assignment.
    def visitAssignment(self, ctx:pandaQParser.AssignmentContext):
        self.instruction_type = "assignment"
        [table_name,_,query] = list(ctx.getChildren())
        self.visit(query)
        self.dataframes[self.visit(table_name)] = self.resultado


    # Visit a parse tree produced by pandaQParser#query.
    def visitQuery(self, ctx:pandaQParser.QueryContext):
        self.instruction_type = "query"
        self.visitChildren(ctx)
        return self.resultado


    # Visit a parse tree produced by pandaQParser#statement.
    def visitStatement(self, ctx:pandaQParser.StatementContext):
        contexts = list(ctx.getChildren())
        self.visit(contexts[3]) # visitar la tabla
        contexts.remove(contexts[3])
        for context in contexts:
            self.visit(context)
            
    # Visit a parse tree produced by pandaQParser#all.
    def visitAll(self, ctx:pandaQParser.AllContext):
        self.resultado = self.source

    # Visit a parse tree produced by pandaQParser#selection.
    def visitSelection(self, ctx:pandaQParser.SelectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#selectItemColumnName.
    def visitSelectItemColumnName(self, ctx:pandaQParser.SelectItemColumnNameContext):
        column_name = self.visitChildren(ctx)
        self.resultado[column_name] = self.source[column_name]

    # Visit a parse tree produced by pandaQParser#selectItemAS.
    def visitSelectItemAS(self, ctx:pandaQParser.SelectItemASContext):
        [expression,_,newColumnName] = list(ctx.getChildren())
        newColumn = newColumnName.getText()
        self.resultado[newColumn] = self.visit(expression)

    # Visit a parse tree produced by pandaQParser#expressionAritmetic.
    def visitExpressionAritmetic(self, ctx:pandaQParser.ExpressionAritmeticContext):
        [col, op, num] = list(ctx.getChildren())
        df_col = self.visit(col)
        number = float(num.getText())

        if op.getText() == '+':
            df_col[df_col.columns[0]] = df_col[df_col.columns[0]] + number
        elif op.getText() == '-':
            df_col[df_col.columns[0]] = df_col[df_col.columns[0]] - number
        elif op.getText() == '*':
            df_col[df_col.columns[0]] = df_col[df_col.columns[0]] * number
        elif op.getText() == '/':
            df_col[df_col.columns[0]] = df_col[df_col.columns[0]] / number
        return df_col


    # Visit a parse tree produced by pandaQParser#expressionColumnName.
    def visitExpressionColumnName(self, ctx:pandaQParser.ExpressionColumnNameContext):
        column_name = self.visitChildren(ctx)
        return self.source[column_name].to_frame()


    # Visit a parse tree produced by pandaQParser#columnName.
    def visitColumnName(self, ctx:pandaQParser.ColumnNameContext):
        return ctx.getText()


    # Visit a parse tree produced by pandaQParser#tableSourceSimple.
    def visitTableSourceSimple(self, ctx:pandaQParser.TableSourceSimpleContext):
        table_name = self.visitChildren(ctx)
        self.source = self.dataframes.get(table_name, pd.DataFrame())

    # Visit a parse tree produced by pandaQParser#tableSourceJoin.
    def visitTableSourceJoin(self, ctx:pandaQParser.TableSourceJoinContext):
        if self.source.empty:
            [table1,_,_,table2,_,joinCondition] = list(ctx.getChildren())
            table1df = self.dataframes.get(self.visit(table1), pd.DataFrame())
            table2df = self.dataframes.get(self.visit(table2), pd.DataFrame())
            joinCondition = self.visit(joinCondition)
            self.source = pd.merge(table1df, table2df, how='inner', on=joinCondition)
        else:
            [_,_,table2,_,joinCondition] = list(ctx.getChildren())
            table2df = self.dataframes.get(self.visit(table2), pd.DataFrame())
            joinCondition = self.visit(joinCondition)
            self.source = pd.merge(self.source, table2df, how='inner', on=joinCondition)
            
        
    def filtradoColumnas(self):
        df_result = pd.DataFrame()

        for seleccion in self.selection:
            partes = seleccion.split(' AS ')
            if len(partes) == 2:
                nombre_columna, nuevo_nombre = partes
            else:
                nombre_columna = seleccion
                nuevo_nombre = seleccion

            df_result[nuevo_nombre] = self.source[nombre_columna] 
        return df_result
        
    # Visit a parse tree produced by pandaQParser#tableName.
    def visitTableName(self, ctx:pandaQParser.TableNameContext):
        return ctx.ID().getText()

    # Visit a parse tree produced by pandaQParser#orderByExpressionList.
    def visitOrderByExpressionList(self, ctx:pandaQParser.OrderByExpressionListContext):
        self.visitChildren(ctx)
        ordered_result = self.resultado.copy()

        if not ordered_result.empty:
            ordered_result.sort_values(by=self.order_columns, ascending=[dir == 'ASC' for dir in self.directions], inplace=True)
        self.resultado = ordered_result

    # Visit a parse tree produced by pandaQParser#orderByExpression.
    def visitOrderByExpression(self, ctx:pandaQParser.OrderByExpressionContext):
        direction = 'ASC'
        children = list(ctx.getChildren())
        column = self.visit(children[0])
        if len(children) == 2:
            direction = children[1].getText().upper()
        self.order_columns.append(column)
        self.directions.append(direction)
        

    # Visit a parse tree produced by pandaQParser#conditionBoolean.
    def visitConditionBoolean(self, ctx:pandaQParser.ConditionBooleanContext):
        self.visitChildren(ctx)
        aux = self.resultado.copy()
        self.resultado = aux[self.where['aux_col']] #Creo una tabla booleana final para filtrar la tabla original
        

    # Visit a parse tree produced by pandaQParser#conditionEqual.
    def visitConditionEqual(self, ctx:pandaQParser.ConditionEqualContext):
        [column1ctx,_,column2ctx] = list(ctx.getChildren())
        column1 = self.visit(column1ctx)
        column2 = self.visit(column2ctx)
        return [column1, column2]


    # Visit a parse tree produced by pandaQParser#conditionIn.
    def visitConditionIn(self, ctx:pandaQParser.ConditionInContext):
        [columnctx,_,_,queryctx,_] = list(ctx.getChildren())
        subquery_visitor = pandaQVisitor(dataframes=self.dataframes)
        # Visitar la subquery con la nueva instancia

        subquery_df = subquery_visitor.visit(queryctx)
        column_name = self.visit(columnctx)
        
        boolean_condition = self.source[column_name].isin(subquery_df[subquery_df.columns[0]])

        # Filtrar self.resultado utilizando el DataFrame booleano
        self.resultado = self.resultado[boolean_condition]
        
        
    # Visit a parse tree produced by pandaQParser#booleanExpression.
    def visitBooleanExpression(self, ctx:pandaQParser.BooleanExpressionContext):
        self.visitChildren(ctx)
        self.where['aux_col'] = self.where.any(axis=1) #Junte de las columnas con logica OR
        self.where = self.where[['aux_col']]
        
    # Visit a parse tree produced by pandaQParser#booleanTerm.
    def visitBooleanTerm(self, ctx:pandaQParser.BooleanTermContext):
        self.visitChildren(ctx)
        self.where['aux_col'] = self.where.all(axis=1) #Junte de las columnas con logica AND
        self.where = self.where[['aux_col']]

        
    # Visit a parse tree produced by pandaQParser#booleanFactor.
    def visitBooleanFactor(self, ctx:pandaQParser.BooleanFactorContext):
        childs = list(ctx.getChildren())
        if len(childs) == 2: #Quiere decir que hay un not, entonces hay que negar el resultado
            self.visit(childs[1])
            self.where = ~self.where
        else:
            self.visit(childs[0])


    # Visit a parse tree produced by pandaQParser#booleanPrimaryBoolean.
    def visitBooleanPrimaryBoolean(self, ctx:pandaQParser.BooleanPrimaryBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#booleanPrimaryComparison.
    def visitBooleanPrimaryComparison(self, ctx:pandaQParser.BooleanPrimaryComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:pandaQParser.ComparisonExpressionContext):
        [columnctx, opctx, valuectx] = list(ctx.getChildren())
        column = self.visit(columnctx)
        op = opctx.getText()
        value = self.visit(valuectx)
        condition = None

        if op == '=':
            condition = self.source[column] == value
        elif op == '<>':
            condition = self.source[column] != value
        elif op == '<':
            condition = self.source[column] < value
        elif op == '>':
            condition = self.source[column] > value
        elif op == '<=':
            condition = self.source[column] <= value
        elif op == '>=':
            condition = self.source[column] >= value
        else:
            print(f"Advertencia: Operador no soportado: {op}")
            
        new_column_name = f"{column}_{op}_{value}"
        if self.where.empty:  
            self.where[new_column_name] = condition
        else:
            self.where[new_column_name] = condition
            
        
    # Visit a parse tree produced by pandaQParser#valueNumber.
    def visitValueNumber(self, ctx:pandaQParser.ValueNumberContext):
        return float(ctx.getText())


    # Visit a parse tree produced by pandaQParser#valueTrue.
    def visitValueTrue(self, ctx:pandaQParser.ValueTrueContext):
        return True


    # Visit a parse tree produced by pandaQParser#valueFalse.
    def visitValueFalse(self, ctx:pandaQParser.ValueFalseContext):
        return False


    # Visit a parse tree produced by pandaQParser#valueString.
    def visitValueString(self, ctx:pandaQParser.ValueStringContext):
        return ctx.ID().getText()
    
    def get_result(self):
        return self.resultado
    
    def reset(self):
        self.instruction_type = None
        self.resultado = pd.DataFrame()
        self.source = pd.DataFrame()
        self.orderBy = []
        self.where = pd.DataFrame()
        
del pandaQParser