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
        4,1,18,93,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,3,0,23,8,0,1,0,1,0,1,1,1,1,1,1,
        1,1,5,1,31,8,1,10,1,12,1,34,9,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,45,8,2,1,3,1,3,1,3,3,3,50,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,5,3,64,8,3,10,3,12,3,67,9,3,1,4,1,4,1,4,5,
        4,72,8,4,10,4,12,4,75,9,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,5,7,84,8,7,
        10,7,12,7,87,9,7,1,8,1,8,3,8,91,8,8,1,8,0,1,6,9,0,2,4,6,8,10,12,
        14,16,0,1,1,0,6,7,95,0,18,1,0,0,0,2,26,1,0,0,0,4,44,1,0,0,0,6,49,
        1,0,0,0,8,68,1,0,0,0,10,76,1,0,0,0,12,78,1,0,0,0,14,80,1,0,0,0,16,
        88,1,0,0,0,18,22,3,2,1,0,19,20,5,4,0,0,20,21,5,5,0,0,21,23,3,14,
        7,0,22,19,1,0,0,0,22,23,1,0,0,0,23,24,1,0,0,0,24,25,5,10,0,0,25,
        1,1,0,0,0,26,27,5,1,0,0,27,32,3,4,2,0,28,29,5,9,0,0,29,31,3,4,2,
        0,30,28,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,35,
        1,0,0,0,34,32,1,0,0,0,35,36,5,2,0,0,36,37,3,12,6,0,37,3,1,0,0,0,
        38,45,5,8,0,0,39,45,3,8,4,0,40,41,3,6,3,0,41,42,5,3,0,0,42,43,3,
        10,5,0,43,45,1,0,0,0,44,38,1,0,0,0,44,39,1,0,0,0,44,40,1,0,0,0,45,
        5,1,0,0,0,46,47,6,3,-1,0,47,50,5,17,0,0,48,50,3,10,5,0,49,46,1,0,
        0,0,49,48,1,0,0,0,50,65,1,0,0,0,51,52,10,5,0,0,52,53,5,8,0,0,53,
        64,3,6,3,6,54,55,10,4,0,0,55,56,5,13,0,0,56,64,3,6,3,5,57,58,10,
        3,0,0,58,59,5,14,0,0,59,64,3,6,3,4,60,61,10,2,0,0,61,62,5,15,0,0,
        62,64,3,6,3,3,63,51,1,0,0,0,63,54,1,0,0,0,63,57,1,0,0,0,63,60,1,
        0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,7,1,0,0,0,67,
        65,1,0,0,0,68,73,3,10,5,0,69,70,5,9,0,0,70,72,3,10,5,0,71,69,1,0,
        0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,9,1,0,0,0,75,73,
        1,0,0,0,76,77,5,16,0,0,77,11,1,0,0,0,78,79,5,16,0,0,79,13,1,0,0,
        0,80,85,3,16,8,0,81,82,5,9,0,0,82,84,3,16,8,0,83,81,1,0,0,0,84,87,
        1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,15,1,0,0,0,87,85,1,0,0,0,
        88,90,3,10,5,0,89,91,7,0,0,0,90,89,1,0,0,0,90,91,1,0,0,0,91,17,1,
        0,0,0,9,22,32,44,49,63,65,73,85,90
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'SELECT'", "'FROM'", "'AS'", "'ORDER'", 
                     "'BY'", "'ASC'", "'DESC'", "'*'", "','", "';'", "'('", 
                     "')'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "AS", "ORDER", "BY", 
                      "ASC", "DESC", "STAR", "COMMA", "SEMICOLON", "LPAREN", 
                      "RPAREN", "DIV", "PLUS", "MINUS", "ID", "NUMBER", 
                      "WS" ]

    RULE_query = 0
    RULE_statement = 1
    RULE_selectItem = 2
    RULE_expression = 3
    RULE_columnNameList = 4
    RULE_columnName = 5
    RULE_tableName = 6
    RULE_orderByExpressionList = 7
    RULE_orderByExpression = 8

    ruleNames =  [ "query", "statement", "selectItem", "expression", "columnNameList", 
                   "columnName", "tableName", "orderByExpressionList", "orderByExpression" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    AS=3
    ORDER=4
    BY=5
    ASC=6
    DESC=7
    STAR=8
    COMMA=9
    SEMICOLON=10
    LPAREN=11
    RPAREN=12
    DIV=13
    PLUS=14
    MINUS=15
    ID=16
    NUMBER=17
    WS=18

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

        def ORDER(self):
            return self.getToken(lcParser.ORDER, 0)

        def BY(self):
            return self.getToken(lcParser.BY, 0)

        def orderByExpressionList(self):
            return self.getTypedRuleContext(lcParser.OrderByExpressionListContext,0)


        def getRuleIndex(self):
            return lcParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = lcParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.statement()
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 19
                self.match(lcParser.ORDER)
                self.state = 20
                self.match(lcParser.BY)
                self.state = 21
                self.orderByExpressionList()


            self.state = 24
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


        def selectItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.SelectItemContext)
            else:
                return self.getTypedRuleContext(lcParser.SelectItemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.COMMA)
            else:
                return self.getToken(lcParser.COMMA, i)

        def getRuleIndex(self):
            return lcParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = lcParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(lcParser.SELECT)

            self.state = 27
            self.selectItem()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 28
                self.match(lcParser.COMMA)
                self.state = 29
                self.selectItem()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(lcParser.FROM)
            self.state = 36
            self.tableName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(lcParser.STAR, 0)

        def columnNameList(self):
            return self.getTypedRuleContext(lcParser.ColumnNameListContext,0)


        def expression(self):
            return self.getTypedRuleContext(lcParser.ExpressionContext,0)


        def AS(self):
            return self.getToken(lcParser.AS, 0)

        def columnName(self):
            return self.getTypedRuleContext(lcParser.ColumnNameContext,0)


        def getRuleIndex(self):
            return lcParser.RULE_selectItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectItem" ):
                listener.enterSelectItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectItem" ):
                listener.exitSelectItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectItem" ):
                return visitor.visitSelectItem(self)
            else:
                return visitor.visitChildren(self)




    def selectItem(self):

        localctx = lcParser.SelectItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_selectItem)
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(lcParser.STAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.columnNameList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.expression(0)
                self.state = 41
                self.match(lcParser.AS)
                self.state = 42
                self.columnName()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(lcParser.NUMBER, 0)

        def columnName(self):
            return self.getTypedRuleContext(lcParser.ColumnNameContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(lcParser.ExpressionContext,i)


        def STAR(self):
            return self.getToken(lcParser.STAR, 0)

        def DIV(self):
            return self.getToken(lcParser.DIV, 0)

        def PLUS(self):
            return self.getToken(lcParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(lcParser.MINUS, 0)

        def getRuleIndex(self):
            return lcParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = lcParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 47
                self.match(lcParser.NUMBER)
                pass
            elif token in [16]:
                self.state = 48
                self.columnName()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 63
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = lcParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 51
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 52
                        self.match(lcParser.STAR)
                        self.state = 53
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = lcParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 54
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 55
                        self.match(lcParser.DIV)
                        self.state = 56
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = lcParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 57
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 58
                        self.match(lcParser.PLUS)
                        self.state = 59
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = lcParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 60
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 61
                        self.match(lcParser.MINUS)
                        self.state = 62
                        self.expression(3)
                        pass

             
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnNameList" ):
                listener.enterColumnNameList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnNameList" ):
                listener.exitColumnNameList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnNameList" ):
                return visitor.visitColumnNameList(self)
            else:
                return visitor.visitChildren(self)




    def columnNameList(self):

        localctx = lcParser.ColumnNameListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_columnNameList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.columnName()
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 69
                    self.match(lcParser.COMMA)
                    self.state = 70
                    self.columnName() 
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnName" ):
                listener.enterColumnName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnName" ):
                listener.exitColumnName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnName" ):
                return visitor.visitColumnName(self)
            else:
                return visitor.visitChildren(self)




    def columnName(self):

        localctx = lcParser.ColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableName" ):
                listener.enterTableName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableName" ):
                listener.exitTableName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableName" ):
                return visitor.visitTableName(self)
            else:
                return visitor.visitChildren(self)




    def tableName(self):

        localctx = lcParser.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(lcParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderByExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orderByExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.OrderByExpressionContext)
            else:
                return self.getTypedRuleContext(lcParser.OrderByExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.COMMA)
            else:
                return self.getToken(lcParser.COMMA, i)

        def getRuleIndex(self):
            return lcParser.RULE_orderByExpressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderByExpressionList" ):
                listener.enterOrderByExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderByExpressionList" ):
                listener.exitOrderByExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderByExpressionList" ):
                return visitor.visitOrderByExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def orderByExpressionList(self):

        localctx = lcParser.OrderByExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_orderByExpressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.orderByExpression()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 81
                self.match(lcParser.COMMA)
                self.state = 82
                self.orderByExpression()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderByExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(lcParser.ColumnNameContext,0)


        def ASC(self):
            return self.getToken(lcParser.ASC, 0)

        def DESC(self):
            return self.getToken(lcParser.DESC, 0)

        def getRuleIndex(self):
            return lcParser.RULE_orderByExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderByExpression" ):
                listener.enterOrderByExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderByExpression" ):
                listener.exitOrderByExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderByExpression" ):
                return visitor.visitOrderByExpression(self)
            else:
                return visitor.visitChildren(self)




    def orderByExpression(self):

        localctx = lcParser.OrderByExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_orderByExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.columnName()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==7:
                self.state = 89
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




