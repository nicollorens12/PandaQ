# Generated from lc.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,34,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,
        1,1,1,1,3,1,17,8,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,25,8,2,10,2,12,2,
        28,9,2,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,0,30,0,10,1,0,0,0,2,
        13,1,0,0,0,4,21,1,0,0,0,6,29,1,0,0,0,8,31,1,0,0,0,10,11,3,2,1,0,
        11,12,5,5,0,0,12,1,1,0,0,0,13,16,5,1,0,0,14,17,5,3,0,0,15,17,3,4,
        2,0,16,14,1,0,0,0,16,15,1,0,0,0,17,18,1,0,0,0,18,19,5,2,0,0,19,20,
        3,8,4,0,20,3,1,0,0,0,21,26,3,6,3,0,22,23,5,4,0,0,23,25,3,6,3,0,24,
        22,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,5,1,0,0,
        0,28,26,1,0,0,0,29,30,5,6,0,0,30,7,1,0,0,0,31,32,5,6,0,0,32,9,1,
        0,0,0,2,16,26
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'SELECT'", "'FROM'", "'*'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "STAR", "COMMA", "SEMICOLON", 
                      "ID", "WS" ]

    RULE_query = 0
    RULE_statement = 1
    RULE_columnNameList = 2
    RULE_columnName = 3
    RULE_tableName = 4

    ruleNames =  [ "query", "statement", "columnNameList", "columnName", 
                   "tableName" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    STAR=3
    COMMA=4
    SEMICOLON=5
    ID=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(lcParser.StatementContext,0)


        def SEMICOLON(self):
            return self.getToken(lcParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return lcParser.RULE_query

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = lcParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.statement()
            self.state = 11
            self.match(lcParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(lcParser.SELECT, 0)

        def FROM(self):
            return self.getToken(lcParser.FROM, 0)

        def tableName(self):
            return self.getTypedRuleContext(lcParser.TableNameContext,0)


        def STAR(self):
            return self.getToken(lcParser.STAR, 0)

        def columnNameList(self):
            return self.getTypedRuleContext(lcParser.ColumnNameListContext,0)


        def getRuleIndex(self):
            return lcParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = lcParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(lcParser.SELECT)
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 14
                self.match(lcParser.STAR)
                pass
            elif token in [6]:
                self.state = 15
                self.columnNameList()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 18
            self.match(lcParser.FROM)
            self.state = 19
            self.tableName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnNameListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(lcParser.ColumnNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.COMMA)
            else:
                return self.getToken(lcParser.COMMA, i)

        def getRuleIndex(self):
            return lcParser.RULE_columnNameList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnNameList" ):
                return visitor.visitColumnNameList(self)
            else:
                return visitor.visitChildren(self)




    def columnNameList(self):

        localctx = lcParser.ColumnNameListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_columnNameList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.columnName()
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 22
                self.match(lcParser.COMMA)
                self.state = 23
                self.columnName()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lcParser.ID, 0)

        def getRuleIndex(self):
            return lcParser.RULE_columnName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnName" ):
                return visitor.visitColumnName(self)
            else:
                return visitor.visitChildren(self)




    def columnName(self):

        localctx = lcParser.ColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(lcParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lcParser.ID, 0)

        def getRuleIndex(self):
            return lcParser.RULE_tableName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableName" ):
                return visitor.visitTableName(self)
            else:
                return visitor.visitChildren(self)




    def tableName(self):

        localctx = lcParser.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(lcParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





