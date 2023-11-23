# Generated from lc.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser

# This class defines a complete generic visitor for a parse tree produced by lcParser.

class lcVisitor(ParseTreeVisitor):
    
    def __init__(self, dataframes):
        self.dataframes = dataframes
        self.current_dataframe = None
        counter = 0
        for dataframe in dataframes:
            counter = counter+1
            print(counter)
            

    # Visit a parse tree produced by lcParser#query.
    def visitQuery(self, ctx:lcParser.QueryContext): 
        print("si")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#statement.
    def visitStatement(self, ctx:lcParser.StatementContext):
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



del lcParser