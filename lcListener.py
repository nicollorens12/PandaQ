# Generated from lc.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser

# This class defines a complete listener for a parse tree produced by lcParser.
class lcListener(ParseTreeListener):

    # Enter a parse tree produced by lcParser#query.
    def enterQuery(self, ctx:lcParser.QueryContext):
        pass

    # Exit a parse tree produced by lcParser#query.
    def exitQuery(self, ctx:lcParser.QueryContext):
        pass


    # Enter a parse tree produced by lcParser#statement.
    def enterStatement(self, ctx:lcParser.StatementContext):
        pass

    # Exit a parse tree produced by lcParser#statement.
    def exitStatement(self, ctx:lcParser.StatementContext):
        pass


    # Enter a parse tree produced by lcParser#selectItem.
    def enterSelectItem(self, ctx:lcParser.SelectItemContext):
        pass

    # Exit a parse tree produced by lcParser#selectItem.
    def exitSelectItem(self, ctx:lcParser.SelectItemContext):
        pass


    # Enter a parse tree produced by lcParser#expression.
    def enterExpression(self, ctx:lcParser.ExpressionContext):
        pass

    # Exit a parse tree produced by lcParser#expression.
    def exitExpression(self, ctx:lcParser.ExpressionContext):
        pass


    # Enter a parse tree produced by lcParser#columnNameList.
    def enterColumnNameList(self, ctx:lcParser.ColumnNameListContext):
        pass

    # Exit a parse tree produced by lcParser#columnNameList.
    def exitColumnNameList(self, ctx:lcParser.ColumnNameListContext):
        pass


    # Enter a parse tree produced by lcParser#columnName.
    def enterColumnName(self, ctx:lcParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by lcParser#columnName.
    def exitColumnName(self, ctx:lcParser.ColumnNameContext):
        pass


    # Enter a parse tree produced by lcParser#tableName.
    def enterTableName(self, ctx:lcParser.TableNameContext):
        pass

    # Exit a parse tree produced by lcParser#tableName.
    def exitTableName(self, ctx:lcParser.TableNameContext):
        pass


    # Enter a parse tree produced by lcParser#orderByExpressionList.
    def enterOrderByExpressionList(self, ctx:lcParser.OrderByExpressionListContext):
        pass

    # Exit a parse tree produced by lcParser#orderByExpressionList.
    def exitOrderByExpressionList(self, ctx:lcParser.OrderByExpressionListContext):
        pass


    # Enter a parse tree produced by lcParser#orderByExpression.
    def enterOrderByExpression(self, ctx:lcParser.OrderByExpressionContext):
        pass

    # Exit a parse tree produced by lcParser#orderByExpression.
    def exitOrderByExpression(self, ctx:lcParser.OrderByExpressionContext):
        pass



del lcParser