# Generated from lc.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser

# This class defines a complete generic visitor for a parse tree produced by lcParser.

class lcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lcParser#query.
    def visitQuery(self, ctx:lcParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#statement.
    def visitStatement(self, ctx:lcParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#selectItem.
    def visitSelectItem(self, ctx:lcParser.SelectItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#expression.
    def visitExpression(self, ctx:lcParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#columnNameList.
    def visitColumnNameList(self, ctx:lcParser.ColumnNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#columnName.
    def visitColumnName(self, ctx:lcParser.ColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#tableName.
    def visitTableName(self, ctx:lcParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#orderByExpressionList.
    def visitOrderByExpressionList(self, ctx:lcParser.OrderByExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#orderByExpression.
    def visitOrderByExpression(self, ctx:lcParser.OrderByExpressionContext):
        return self.visitChildren(ctx)



del lcParser