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
        4,1,34,161,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,3,0,37,8,0,1,0,1,0,1,1,1,1,1,
        1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,1,1,1,1,1,1,1,3,1,54,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,3,2,62,8,2,1,3,1,3,1,3,3,3,67,8,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,81,8,3,10,3,12,3,84,9,
        3,1,4,1,4,1,4,5,4,89,8,4,10,4,12,4,92,9,4,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,5,6,103,8,6,10,6,12,6,106,9,6,1,7,1,7,1,8,1,8,1,8,
        5,8,113,8,8,10,8,12,8,116,9,8,1,9,1,9,3,9,120,8,9,1,10,1,10,1,10,
        1,10,1,10,3,10,127,8,10,1,11,1,11,1,11,5,11,132,8,11,10,11,12,11,
        135,9,11,1,12,1,12,1,12,5,12,140,8,12,10,12,12,12,143,9,12,1,13,
        3,13,146,8,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,14,155,8,14,1,
        15,1,15,1,15,1,15,1,15,0,1,6,16,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,0,3,1,0,6,7,1,0,23,28,1,0,30,33,163,0,32,1,0,0,0,2,40,1,
        0,0,0,4,61,1,0,0,0,6,66,1,0,0,0,8,85,1,0,0,0,10,93,1,0,0,0,12,95,
        1,0,0,0,14,107,1,0,0,0,16,109,1,0,0,0,18,117,1,0,0,0,20,126,1,0,
        0,0,22,128,1,0,0,0,24,136,1,0,0,0,26,145,1,0,0,0,28,154,1,0,0,0,
        30,156,1,0,0,0,32,36,3,2,1,0,33,34,5,4,0,0,34,35,5,5,0,0,35,37,3,
        16,8,0,36,33,1,0,0,0,36,37,1,0,0,0,37,38,1,0,0,0,38,39,5,17,0,0,
        39,1,1,0,0,0,40,41,5,1,0,0,41,46,3,4,2,0,42,43,5,16,0,0,43,45,3,
        4,2,0,44,42,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,
        49,1,0,0,0,48,46,1,0,0,0,49,50,5,2,0,0,50,53,3,12,6,0,51,52,5,8,
        0,0,52,54,3,20,10,0,53,51,1,0,0,0,53,54,1,0,0,0,54,3,1,0,0,0,55,
        62,5,15,0,0,56,62,3,8,4,0,57,58,3,6,3,0,58,59,5,3,0,0,59,60,3,10,
        5,0,60,62,1,0,0,0,61,55,1,0,0,0,61,56,1,0,0,0,61,57,1,0,0,0,62,5,
        1,0,0,0,63,64,6,3,-1,0,64,67,5,30,0,0,65,67,3,10,5,0,66,63,1,0,0,
        0,66,65,1,0,0,0,67,82,1,0,0,0,68,69,10,5,0,0,69,70,5,15,0,0,70,81,
        3,6,3,6,71,72,10,4,0,0,72,73,5,20,0,0,73,81,3,6,3,5,74,75,10,3,0,
        0,75,76,5,21,0,0,76,81,3,6,3,4,77,78,10,2,0,0,78,79,5,22,0,0,79,
        81,3,6,3,3,80,68,1,0,0,0,80,71,1,0,0,0,80,74,1,0,0,0,80,77,1,0,0,
        0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,7,1,0,0,0,84,82,1,
        0,0,0,85,90,3,10,5,0,86,87,5,16,0,0,87,89,3,10,5,0,88,86,1,0,0,0,
        89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,9,1,0,0,0,92,90,1,0,
        0,0,93,94,5,29,0,0,94,11,1,0,0,0,95,104,3,14,7,0,96,97,5,12,0,0,
        97,98,5,13,0,0,98,99,3,14,7,0,99,100,5,14,0,0,100,101,3,20,10,0,
        101,103,1,0,0,0,102,96,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,
        105,1,0,0,0,105,13,1,0,0,0,106,104,1,0,0,0,107,108,5,29,0,0,108,
        15,1,0,0,0,109,114,3,18,9,0,110,111,5,16,0,0,111,113,3,18,9,0,112,
        110,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,
        17,1,0,0,0,116,114,1,0,0,0,117,119,3,10,5,0,118,120,7,0,0,0,119,
        118,1,0,0,0,119,120,1,0,0,0,120,19,1,0,0,0,121,127,3,22,11,0,122,
        123,3,10,5,0,123,124,5,23,0,0,124,125,3,10,5,0,125,127,1,0,0,0,126,
        121,1,0,0,0,126,122,1,0,0,0,127,21,1,0,0,0,128,133,3,24,12,0,129,
        130,5,9,0,0,130,132,3,24,12,0,131,129,1,0,0,0,132,135,1,0,0,0,133,
        131,1,0,0,0,133,134,1,0,0,0,134,23,1,0,0,0,135,133,1,0,0,0,136,141,
        3,26,13,0,137,138,5,10,0,0,138,140,3,26,13,0,139,137,1,0,0,0,140,
        143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,25,1,0,0,0,143,141,
        1,0,0,0,144,146,5,11,0,0,145,144,1,0,0,0,145,146,1,0,0,0,146,147,
        1,0,0,0,147,148,3,28,14,0,148,27,1,0,0,0,149,150,5,18,0,0,150,151,
        3,22,11,0,151,152,5,19,0,0,152,155,1,0,0,0,153,155,3,30,15,0,154,
        149,1,0,0,0,154,153,1,0,0,0,155,29,1,0,0,0,156,157,3,10,5,0,157,
        158,7,1,0,0,158,159,7,2,0,0,159,31,1,0,0,0,16,36,46,53,61,66,80,
        82,90,104,114,119,126,133,141,145,154
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'*'", "','", 
                     "';'", "'('", "')'", "'/'", "'+'", "'-'", "'='", "'<>'", 
                     "'<'", "'<='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "AS", "ORDER", "BY", 
                      "ASC", "DESC", "WHERE", "OR", "AND", "NOT", "INNER", 
                      "JOIN", "ON", "STAR", "COMMA", "SEMICOLON", "LPAREN", 
                      "RPAREN", "DIV", "PLUS", "MINUS", "EQUAL", "NOT_EQUAL", 
                      "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
                      "ID", "NUMBER", "STRING", "TRUE", "FALSE", "WS" ]

    RULE_query = 0
    RULE_statement = 1
    RULE_selectItem = 2
    RULE_expression = 3
    RULE_columnNameList = 4
    RULE_columnName = 5
    RULE_tableSource = 6
    RULE_tableName = 7
    RULE_orderByExpressionList = 8
    RULE_orderByExpression = 9
    RULE_condition = 10
    RULE_booleanExpression = 11
    RULE_booleanTerm = 12
    RULE_booleanFactor = 13
    RULE_booleanPrimary = 14
    RULE_comparisonExpression = 15

    ruleNames =  [ "query", "statement", "selectItem", "expression", "columnNameList", 
                   "columnName", "tableSource", "tableName", "orderByExpressionList", 
                   "orderByExpression", "condition", "booleanExpression", 
                   "booleanTerm", "booleanFactor", "booleanPrimary", "comparisonExpression" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    AS=3
    ORDER=4
    BY=5
    ASC=6
    DESC=7
    WHERE=8
    OR=9
    AND=10
    NOT=11
    INNER=12
    JOIN=13
    ON=14
    STAR=15
    COMMA=16
    SEMICOLON=17
    LPAREN=18
    RPAREN=19
    DIV=20
    PLUS=21
    MINUS=22
    EQUAL=23
    NOT_EQUAL=24
    LESS=25
    LESS_OR_EQUAL=26
    GREATER=27
    GREATER_OR_EQUAL=28
    ID=29
    NUMBER=30
    STRING=31
    TRUE=32
    FALSE=33
    WS=34

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
            self.state = 32
            self.statement()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 33
                self.match(lcParser.ORDER)
                self.state = 34
                self.match(lcParser.BY)
                self.state = 35
                self.orderByExpressionList()


            self.state = 38
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

        def tableSource(self):
            return self.getTypedRuleContext(lcParser.TableSourceContext,0)


        def selectItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.SelectItemContext)
            else:
                return self.getTypedRuleContext(lcParser.SelectItemContext,i)


        def WHERE(self):
            return self.getToken(lcParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(lcParser.ConditionContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.COMMA)
            else:
                return self.getToken(lcParser.COMMA, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(lcParser.SELECT)

            self.state = 41
            self.selectItem()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 42
                self.match(lcParser.COMMA)
                self.state = 43
                self.selectItem()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(lcParser.FROM)
            self.state = 50
            self.tableSource()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 51
                self.match(lcParser.WHERE)
                self.state = 52
                self.condition()


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectItem" ):
                return visitor.visitSelectItem(self)
            else:
                return visitor.visitChildren(self)




    def selectItem(self):

        localctx = lcParser.SelectItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_selectItem)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(lcParser.STAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.columnNameList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.expression(0)
                self.state = 58
                self.match(lcParser.AS)
                self.state = 59
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
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.state = 64
                self.match(lcParser.NUMBER)
                pass
            elif token in [29]:
                self.state = 65
                self.columnName()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 80
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = lcParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 68
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 69
                        self.match(lcParser.STAR)
                        self.state = 70
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = lcParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 71
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 72
                        self.match(lcParser.DIV)
                        self.state = 73
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = lcParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 74
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 75
                        self.match(lcParser.PLUS)
                        self.state = 76
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = lcParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 77
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 78
                        self.match(lcParser.MINUS)
                        self.state = 79
                        self.expression(3)
                        pass

             
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
            self.state = 85
            self.columnName()
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 86
                    self.match(lcParser.COMMA)
                    self.state = 87
                    self.columnName() 
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 10, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(lcParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableSourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.TableNameContext)
            else:
                return self.getTypedRuleContext(lcParser.TableNameContext,i)


        def INNER(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.INNER)
            else:
                return self.getToken(lcParser.INNER, i)

        def JOIN(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.JOIN)
            else:
                return self.getToken(lcParser.JOIN, i)

        def ON(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.ON)
            else:
                return self.getToken(lcParser.ON, i)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.ConditionContext)
            else:
                return self.getTypedRuleContext(lcParser.ConditionContext,i)


        def getRuleIndex(self):
            return lcParser.RULE_tableSource

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableSource" ):
                return visitor.visitTableSource(self)
            else:
                return visitor.visitChildren(self)




    def tableSource(self):

        localctx = lcParser.TableSourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tableSource)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.tableName()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 96
                self.match(lcParser.INNER)
                self.state = 97
                self.match(lcParser.JOIN)
                self.state = 98
                self.tableName()
                self.state = 99
                self.match(lcParser.ON)
                self.state = 100
                self.condition()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 14, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderByExpressionList" ):
                return visitor.visitOrderByExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def orderByExpressionList(self):

        localctx = lcParser.OrderByExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_orderByExpressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.orderByExpression()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 110
                self.match(lcParser.COMMA)
                self.state = 111
                self.orderByExpression()
                self.state = 116
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderByExpression" ):
                return visitor.visitOrderByExpression(self)
            else:
                return visitor.visitChildren(self)




    def orderByExpression(self):

        localctx = lcParser.OrderByExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_orderByExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.columnName()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==7:
                self.state = 118
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


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanExpression(self):
            return self.getTypedRuleContext(lcParser.BooleanExpressionContext,0)


        def columnName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(lcParser.ColumnNameContext,i)


        def EQUAL(self):
            return self.getToken(lcParser.EQUAL, 0)

        def getRuleIndex(self):
            return lcParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = lcParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condition)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.booleanExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.columnName()
                self.state = 123
                self.match(lcParser.EQUAL)
                self.state = 124
                self.columnName()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.BooleanTermContext)
            else:
                return self.getTypedRuleContext(lcParser.BooleanTermContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.OR)
            else:
                return self.getToken(lcParser.OR, i)

        def getRuleIndex(self):
            return lcParser.RULE_booleanExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanExpression" ):
                return visitor.visitBooleanExpression(self)
            else:
                return visitor.visitChildren(self)




    def booleanExpression(self):

        localctx = lcParser.BooleanExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_booleanExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.booleanTerm()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 129
                self.match(lcParser.OR)
                self.state = 130
                self.booleanTerm()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanFactor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.BooleanFactorContext)
            else:
                return self.getTypedRuleContext(lcParser.BooleanFactorContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.AND)
            else:
                return self.getToken(lcParser.AND, i)

        def getRuleIndex(self):
            return lcParser.RULE_booleanTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanTerm" ):
                return visitor.visitBooleanTerm(self)
            else:
                return visitor.visitChildren(self)




    def booleanTerm(self):

        localctx = lcParser.BooleanTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_booleanTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.booleanFactor()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 137
                self.match(lcParser.AND)
                self.state = 138
                self.booleanFactor()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanPrimary(self):
            return self.getTypedRuleContext(lcParser.BooleanPrimaryContext,0)


        def NOT(self):
            return self.getToken(lcParser.NOT, 0)

        def getRuleIndex(self):
            return lcParser.RULE_booleanFactor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanFactor" ):
                return visitor.visitBooleanFactor(self)
            else:
                return visitor.visitChildren(self)




    def booleanFactor(self):

        localctx = lcParser.BooleanFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_booleanFactor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 144
                self.match(lcParser.NOT)


            self.state = 147
            self.booleanPrimary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanPrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(lcParser.LPAREN, 0)

        def booleanExpression(self):
            return self.getTypedRuleContext(lcParser.BooleanExpressionContext,0)


        def RPAREN(self):
            return self.getToken(lcParser.RPAREN, 0)

        def comparisonExpression(self):
            return self.getTypedRuleContext(lcParser.ComparisonExpressionContext,0)


        def getRuleIndex(self):
            return lcParser.RULE_booleanPrimary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanPrimary" ):
                return visitor.visitBooleanPrimary(self)
            else:
                return visitor.visitChildren(self)




    def booleanPrimary(self):

        localctx = lcParser.BooleanPrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_booleanPrimary)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(lcParser.LPAREN)
                self.state = 150
                self.booleanExpression()
                self.state = 151
                self.match(lcParser.RPAREN)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.comparisonExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(lcParser.ColumnNameContext,0)


        def EQUAL(self):
            return self.getToken(lcParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(lcParser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(lcParser.LESS, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(lcParser.LESS_OR_EQUAL, 0)

        def GREATER(self):
            return self.getToken(lcParser.GREATER, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(lcParser.GREATER_OR_EQUAL, 0)

        def NUMBER(self):
            return self.getToken(lcParser.NUMBER, 0)

        def TRUE(self):
            return self.getToken(lcParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(lcParser.FALSE, 0)

        def STRING(self):
            return self.getToken(lcParser.STRING, 0)

        def getRuleIndex(self):
            return lcParser.RULE_comparisonExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpression" ):
                return visitor.visitComparisonExpression(self)
            else:
                return visitor.visitChildren(self)




    def comparisonExpression(self):

        localctx = lcParser.ComparisonExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comparisonExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.columnName()
            self.state = 157
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 158
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0)):
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
         




