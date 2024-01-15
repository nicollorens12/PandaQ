# Generated from pandaQ.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .pandaQParser import pandaQParser
else:
    from pandaQParser import pandaQParser

# This class defines a complete generic visitor for a parse tree produced by pandaQParser.

class pandaQVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pandaQParser#instruction.
    def visitInstruction(self, ctx:pandaQParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#plot.
    def visitPlot(self, ctx:pandaQParser.PlotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#assignment.
    def visitAssignment(self, ctx:pandaQParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#query.
    def visitQuery(self, ctx:pandaQParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#statement.
    def visitStatement(self, ctx:pandaQParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#all.
    def visitAll(self, ctx:pandaQParser.AllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#selection.
    def visitSelection(self, ctx:pandaQParser.SelectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#selectItemColumnName.
    def visitSelectItemColumnName(self, ctx:pandaQParser.SelectItemColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#selectItemAS.
    def visitSelectItemAS(self, ctx:pandaQParser.SelectItemASContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#expressionAritmetic.
    def visitExpressionAritmetic(self, ctx:pandaQParser.ExpressionAritmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#expressionColumnName.
    def visitExpressionColumnName(self, ctx:pandaQParser.ExpressionColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#columnName.
    def visitColumnName(self, ctx:pandaQParser.ColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#tableSourceSimple.
    def visitTableSourceSimple(self, ctx:pandaQParser.TableSourceSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#tableSourceJoin.
    def visitTableSourceJoin(self, ctx:pandaQParser.TableSourceJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#tableName.
    def visitTableName(self, ctx:pandaQParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#orderByExpressionList.
    def visitOrderByExpressionList(self, ctx:pandaQParser.OrderByExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#orderByExpression.
    def visitOrderByExpression(self, ctx:pandaQParser.OrderByExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#conditionBoolean.
    def visitConditionBoolean(self, ctx:pandaQParser.ConditionBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#conditionEqual.
    def visitConditionEqual(self, ctx:pandaQParser.ConditionEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#conditionIn.
    def visitConditionIn(self, ctx:pandaQParser.ConditionInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#booleanExpression.
    def visitBooleanExpression(self, ctx:pandaQParser.BooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#booleanTerm.
    def visitBooleanTerm(self, ctx:pandaQParser.BooleanTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#booleanFactor.
    def visitBooleanFactor(self, ctx:pandaQParser.BooleanFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#booleanPrimaryBoolean.
    def visitBooleanPrimaryBoolean(self, ctx:pandaQParser.BooleanPrimaryBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#booleanPrimaryComparison.
    def visitBooleanPrimaryComparison(self, ctx:pandaQParser.BooleanPrimaryComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:pandaQParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#valueNumber.
    def visitValueNumber(self, ctx:pandaQParser.ValueNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#valueTrue.
    def visitValueTrue(self, ctx:pandaQParser.ValueTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#valueFalse.
    def visitValueFalse(self, ctx:pandaQParser.ValueFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#valueString.
    def visitValueString(self, ctx:pandaQParser.ValueStringContext):
        return self.visitChildren(ctx)



del pandaQParser