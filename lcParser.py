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
        4,1,15,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,1,1,1,1,
        1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,45,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,
        3,59,8,3,10,3,12,3,62,9,3,1,4,1,4,1,4,5,4,67,8,4,10,4,12,4,70,9,
        4,1,5,1,5,1,6,1,6,1,6,0,1,6,7,0,2,4,6,8,10,12,0,0,78,0,14,1,0,0,
        0,2,17,1,0,0,0,4,35,1,0,0,0,6,44,1,0,0,0,8,63,1,0,0,0,10,71,1,0,
        0,0,12,73,1,0,0,0,14,15,3,2,1,0,15,16,5,6,0,0,16,1,1,0,0,0,17,18,
        5,1,0,0,18,23,3,4,2,0,19,20,5,5,0,0,20,22,3,4,2,0,21,19,1,0,0,0,
        22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,
        0,0,0,26,27,5,2,0,0,27,28,3,12,6,0,28,3,1,0,0,0,29,36,5,4,0,0,30,
        36,3,8,4,0,31,32,3,6,3,0,32,33,5,3,0,0,33,34,3,10,5,0,34,36,1,0,
        0,0,35,29,1,0,0,0,35,30,1,0,0,0,35,31,1,0,0,0,36,5,1,0,0,0,37,38,
        6,3,-1,0,38,39,5,7,0,0,39,40,3,6,3,0,40,41,5,8,0,0,41,45,1,0,0,0,
        42,45,3,10,5,0,43,45,5,14,0,0,44,37,1,0,0,0,44,42,1,0,0,0,44,43,
        1,0,0,0,45,60,1,0,0,0,46,47,10,6,0,0,47,48,5,9,0,0,48,59,3,6,3,7,
        49,50,10,5,0,0,50,51,5,10,0,0,51,59,3,6,3,6,52,53,10,4,0,0,53,54,
        5,11,0,0,54,59,3,6,3,5,55,56,10,3,0,0,56,57,5,12,0,0,57,59,3,6,3,
        4,58,46,1,0,0,0,58,49,1,0,0,0,58,52,1,0,0,0,58,55,1,0,0,0,59,62,
        1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,7,1,0,0,0,62,60,1,0,0,0,63,
        68,3,10,5,0,64,65,5,5,0,0,65,67,3,10,5,0,66,64,1,0,0,0,67,70,1,0,
        0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,9,1,0,0,0,70,68,1,0,0,0,71,72,
        5,13,0,0,72,11,1,0,0,0,73,74,5,13,0,0,74,13,1,0,0,0,6,23,35,44,58,
        60,68
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'SELECT'", "'FROM'", "'AS'", "<INVALID>", 
                     "','", "';'", "'('", "')'", "<INVALID>", "'/'", "'+'", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "AS", "STAR", "COMMA", 
                      "SEMICOLON", "LPAREN", "RPAREN", "MULT", "DIV", "PLUS", 
                      "MINUS", "ID", "INTEGER", "WS" ]

    RULE_query = 0
    RULE_statement = 1
    RULE_selectItem = 2
    RULE_expression = 3
    RULE_columnNameList = 4
    RULE_columnName = 5
    RULE_tableName = 6

    ruleNames =  [ "query", "statement", "selectItem", "expression", "columnNameList", 
                   "columnName", "tableName" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    AS=3
    STAR=4
    COMMA=5
    SEMICOLON=6
    LPAREN=7
    RPAREN=8
    MULT=9
    DIV=10
    PLUS=11
    MINUS=12
    ID=13
    INTEGER=14
    WS=15

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
            self.state = 14
            self.statement()
            self.state = 15
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
            self.state = 17
            self.match(lcParser.SELECT)

            self.state = 18
            self.selectItem()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 19
                self.match(lcParser.COMMA)
                self.state = 20
                self.selectItem()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(lcParser.FROM)
            self.state = 27
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectItem" ):
                return visitor.visitSelectItem(self)
            else:
                return visitor.visitChildren(self)




    def selectItem(self):

        localctx = lcParser.SelectItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_selectItem)
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(lcParser.STAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.columnNameList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.expression(0)
                self.state = 32
                self.match(lcParser.AS)
                self.state = 33
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

        def LPAREN(self):
            return self.getToken(lcParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(lcParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(lcParser.RPAREN, 0)

        def columnName(self):
            return self.getTypedRuleContext(lcParser.ColumnNameContext,0)


        def INTEGER(self):
            return self.getToken(lcParser.INTEGER, 0)

        def MULT(self):
            return self.getToken(lcParser.MULT, 0)

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
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 38
                self.match(lcParser.LPAREN)
                self.state = 39
                self.expression(0)
                self.state = 40
                self.match(lcParser.RPAREN)
                pass
            elif token in [13]:
                self.state = 42
                self.columnName()
                pass
            elif token in [14]:
                self.state = 43
                self.match(lcParser.INTEGER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 58
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = lcParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 46
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 47
                        self.match(lcParser.MULT)
                        self.state = 48
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = lcParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 49
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 50
                        self.match(lcParser.DIV)
                        self.state = 51
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = lcParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 52
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 53
                        self.match(lcParser.PLUS)
                        self.state = 54
                        self.expression(5)
                        pass

                    elif la_ == 4:
                        localctx = lcParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 55
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 56
                        self.match(lcParser.MINUS)
                        self.state = 57
                        self.expression(4)
                        pass

             
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
            self.state = 63
            self.columnName()
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 64
                    self.match(lcParser.COMMA)
                    self.state = 65
                    self.columnName() 
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
            self.state = 71
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
        self.enterRule(localctx, 12, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(lcParser.ID)
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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




