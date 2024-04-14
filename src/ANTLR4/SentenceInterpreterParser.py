# Generated from ./src/ANTLR4/SentenceInterpreter.g4 by ANTLR 4.13.1
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
        4,1,13,73,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,
        0,14,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,24,8,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,38,8,1,10,1,12,1,41,9,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,71,8,2,1,2,0,
        1,2,3,0,2,4,0,1,1,0,11,12,81,0,13,1,0,0,0,2,23,1,0,0,0,4,70,1,0,
        0,0,6,7,5,4,0,0,7,8,5,11,0,0,8,14,3,0,0,0,9,10,5,5,0,0,10,11,5,11,
        0,0,11,14,3,0,0,0,12,14,3,2,1,0,13,6,1,0,0,0,13,9,1,0,0,0,13,12,
        1,0,0,0,14,1,1,0,0,0,15,16,6,1,-1,0,16,17,5,1,0,0,17,18,3,2,1,0,
        18,19,5,2,0,0,19,24,1,0,0,0,20,21,5,10,0,0,21,24,3,2,1,2,22,24,3,
        4,2,0,23,15,1,0,0,0,23,20,1,0,0,0,23,22,1,0,0,0,24,39,1,0,0,0,25,
        26,10,7,0,0,26,27,5,7,0,0,27,38,3,2,1,8,28,29,10,6,0,0,29,30,5,6,
        0,0,30,38,3,2,1,7,31,32,10,4,0,0,32,33,5,9,0,0,33,38,3,2,1,5,34,
        35,10,3,0,0,35,36,5,8,0,0,36,38,3,2,1,4,37,25,1,0,0,0,37,28,1,0,
        0,0,37,31,1,0,0,0,37,34,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,
        1,0,0,0,40,3,1,0,0,0,41,39,1,0,0,0,42,43,5,12,0,0,43,44,5,1,0,0,
        44,45,7,0,0,0,45,71,5,2,0,0,46,47,5,12,0,0,47,48,5,1,0,0,48,49,5,
        11,0,0,49,50,5,3,0,0,50,51,5,11,0,0,51,71,5,2,0,0,52,53,5,12,0,0,
        53,54,5,1,0,0,54,55,5,11,0,0,55,56,5,3,0,0,56,57,5,12,0,0,57,71,
        5,2,0,0,58,59,5,12,0,0,59,60,5,1,0,0,60,61,5,12,0,0,61,62,5,3,0,
        0,62,63,5,11,0,0,63,71,5,2,0,0,64,65,5,12,0,0,65,66,5,1,0,0,66,67,
        5,12,0,0,67,68,5,3,0,0,68,69,5,12,0,0,69,71,5,2,0,0,70,42,1,0,0,
        0,70,46,1,0,0,0,70,52,1,0,0,0,70,58,1,0,0,0,70,64,1,0,0,0,71,5,1,
        0,0,0,5,13,23,37,39,70
    ]

class SentenceInterpreterParser ( Parser ):

    grammarFileName = "SentenceInterpreter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "<INVALID>", "<INVALID>", 
                     "'=>'", "'<=>'", "<INVALID>", "<INVALID>", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ALL", "EXISTS", "IMPLICATION", "BICONDITIONAL", "OR", 
                      "AND", "NOT", "ID", "PREDICATE", "IGNORED" ]

    RULE_sentencia = 0
    RULE_expression_ = 1
    RULE_predicate_ = 2

    ruleNames =  [ "sentencia", "expression_", "predicate_" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ALL=4
    EXISTS=5
    IMPLICATION=6
    BICONDITIONAL=7
    OR=8
    AND=9
    NOT=10
    ID=11
    PREDICATE=12
    IGNORED=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentenceInterpreterParser.RULE_sentencia

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionContext(SentenciaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.SentenciaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression_(self):
            return self.getTypedRuleContext(SentenceInterpreterParser.Expression_Context,0)


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


    class ExistsContext(SentenciaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.SentenciaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXISTS(self):
            return self.getToken(SentenceInterpreterParser.EXISTS, 0)
        def ID(self):
            return self.getToken(SentenceInterpreterParser.ID, 0)
        def sentencia(self):
            return self.getTypedRuleContext(SentenceInterpreterParser.SentenciaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExists" ):
                listener.enterExists(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExists" ):
                listener.exitExists(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExists" ):
                return visitor.visitExists(self)
            else:
                return visitor.visitChildren(self)


    class ForallContext(SentenciaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.SentenciaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ALL(self):
            return self.getToken(SentenceInterpreterParser.ALL, 0)
        def ID(self):
            return self.getToken(SentenceInterpreterParser.ID, 0)
        def sentencia(self):
            return self.getTypedRuleContext(SentenceInterpreterParser.SentenciaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForall" ):
                listener.enterForall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForall" ):
                listener.exitForall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForall" ):
                return visitor.visitForall(self)
            else:
                return visitor.visitChildren(self)



    def sentencia(self):

        localctx = SentenceInterpreterParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sentencia)
        try:
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = SentenceInterpreterParser.ForallContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.match(SentenceInterpreterParser.ALL)
                self.state = 7
                self.match(SentenceInterpreterParser.ID)
                self.state = 8
                self.sentencia()
                pass
            elif token in [5]:
                localctx = SentenceInterpreterParser.ExistsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.match(SentenceInterpreterParser.EXISTS)
                self.state = 10
                self.match(SentenceInterpreterParser.ID)
                self.state = 11
                self.sentencia()
                pass
            elif token in [1, 10, 12]:
                localctx = SentenceInterpreterParser.ExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 12
                self.expression_(0)
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


    class Expression_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentenceInterpreterParser.RULE_expression_

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParenthesisContext(Expression_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.Expression_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression_(self):
            return self.getTypedRuleContext(SentenceInterpreterParser.Expression_Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis" ):
                listener.enterParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis" ):
                listener.exitParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(Expression_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.Expression_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SentenceInterpreterParser.Expression_Context)
            else:
                return self.getTypedRuleContext(SentenceInterpreterParser.Expression_Context,i)

        def OR(self):
            return self.getToken(SentenceInterpreterParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class NegationContext(Expression_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.Expression_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SentenceInterpreterParser.NOT, 0)
        def expression_(self):
            return self.getTypedRuleContext(SentenceInterpreterParser.Expression_Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation" ):
                listener.enterNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation" ):
                listener.exitNegation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegation" ):
                return visitor.visitNegation(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(Expression_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.Expression_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SentenceInterpreterParser.Expression_Context)
            else:
                return self.getTypedRuleContext(SentenceInterpreterParser.Expression_Context,i)

        def AND(self):
            return self.getToken(SentenceInterpreterParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class BiconditionalContext(Expression_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.Expression_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SentenceInterpreterParser.Expression_Context)
            else:
                return self.getTypedRuleContext(SentenceInterpreterParser.Expression_Context,i)

        def BICONDITIONAL(self):
            return self.getToken(SentenceInterpreterParser.BICONDITIONAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBiconditional" ):
                listener.enterBiconditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBiconditional" ):
                listener.exitBiconditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBiconditional" ):
                return visitor.visitBiconditional(self)
            else:
                return visitor.visitChildren(self)


    class ImplicationContext(Expression_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.Expression_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SentenceInterpreterParser.Expression_Context)
            else:
                return self.getTypedRuleContext(SentenceInterpreterParser.Expression_Context,i)

        def IMPLICATION(self):
            return self.getToken(SentenceInterpreterParser.IMPLICATION, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplication" ):
                listener.enterImplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplication" ):
                listener.exitImplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplication" ):
                return visitor.visitImplication(self)
            else:
                return visitor.visitChildren(self)


    class PredicateContext(Expression_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.Expression_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate_(self):
            return self.getTypedRuleContext(SentenceInterpreterParser.Predicate_Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate" ):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)



    def expression_(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SentenceInterpreterParser.Expression_Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression_, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = SentenceInterpreterParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 16
                self.match(SentenceInterpreterParser.T__0)
                self.state = 17
                self.expression_(0)
                self.state = 18
                self.match(SentenceInterpreterParser.T__1)
                pass
            elif token in [10]:
                localctx = SentenceInterpreterParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(SentenceInterpreterParser.NOT)
                self.state = 21
                self.expression_(2)
                pass
            elif token in [12]:
                localctx = SentenceInterpreterParser.PredicateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.predicate_()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = SentenceInterpreterParser.BiconditionalContext(self, SentenceInterpreterParser.Expression_Context(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_)
                        self.state = 25
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 26
                        self.match(SentenceInterpreterParser.BICONDITIONAL)
                        self.state = 27
                        self.expression_(8)
                        pass

                    elif la_ == 2:
                        localctx = SentenceInterpreterParser.ImplicationContext(self, SentenceInterpreterParser.Expression_Context(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_)
                        self.state = 28
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 29
                        self.match(SentenceInterpreterParser.IMPLICATION)
                        self.state = 30
                        self.expression_(7)
                        pass

                    elif la_ == 3:
                        localctx = SentenceInterpreterParser.AndContext(self, SentenceInterpreterParser.Expression_Context(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_)
                        self.state = 31
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 32
                        self.match(SentenceInterpreterParser.AND)
                        self.state = 33
                        self.expression_(5)
                        pass

                    elif la_ == 4:
                        localctx = SentenceInterpreterParser.OrContext(self, SentenceInterpreterParser.Expression_Context(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_)
                        self.state = 34
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 35
                        self.match(SentenceInterpreterParser.OR)
                        self.state = 36
                        self.expression_(4)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Predicate_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentenceInterpreterParser.RULE_predicate_

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PPContext(Predicate_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.Predicate_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def PREDICATE(self, i:int=None):
            if i is None:
                return self.getTokens(SentenceInterpreterParser.PREDICATE)
            else:
                return self.getToken(SentenceInterpreterParser.PREDICATE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPP" ):
                listener.enterPP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPP" ):
                listener.exitPP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPP" ):
                return visitor.visitPP(self)
            else:
                return visitor.visitChildren(self)


    class UniContext(Predicate_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.Predicate_Context
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def PREDICATE(self, i:int=None):
            if i is None:
                return self.getTokens(SentenceInterpreterParser.PREDICATE)
            else:
                return self.getToken(SentenceInterpreterParser.PREDICATE, i)
        def ID(self):
            return self.getToken(SentenceInterpreterParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUni" ):
                listener.enterUni(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUni" ):
                listener.exitUni(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUni" ):
                return visitor.visitUni(self)
            else:
                return visitor.visitChildren(self)


    class IDIDContext(Predicate_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.Predicate_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def PREDICATE(self):
            return self.getToken(SentenceInterpreterParser.PREDICATE, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SentenceInterpreterParser.ID)
            else:
                return self.getToken(SentenceInterpreterParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIDID" ):
                listener.enterIDID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIDID" ):
                listener.exitIDID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIDID" ):
                return visitor.visitIDID(self)
            else:
                return visitor.visitChildren(self)


    class IDPContext(Predicate_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.Predicate_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def PREDICATE(self, i:int=None):
            if i is None:
                return self.getTokens(SentenceInterpreterParser.PREDICATE)
            else:
                return self.getToken(SentenceInterpreterParser.PREDICATE, i)
        def ID(self):
            return self.getToken(SentenceInterpreterParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIDP" ):
                listener.enterIDP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIDP" ):
                listener.exitIDP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIDP" ):
                return visitor.visitIDP(self)
            else:
                return visitor.visitChildren(self)


    class PIDContext(Predicate_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenceInterpreterParser.Predicate_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def PREDICATE(self, i:int=None):
            if i is None:
                return self.getTokens(SentenceInterpreterParser.PREDICATE)
            else:
                return self.getToken(SentenceInterpreterParser.PREDICATE, i)
        def ID(self):
            return self.getToken(SentenceInterpreterParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPID" ):
                listener.enterPID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPID" ):
                listener.exitPID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPID" ):
                return visitor.visitPID(self)
            else:
                return visitor.visitChildren(self)



    def predicate_(self):

        localctx = SentenceInterpreterParser.Predicate_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_predicate_)
        self._la = 0 # Token type
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = SentenceInterpreterParser.UniContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(SentenceInterpreterParser.PREDICATE)
                self.state = 43
                self.match(SentenceInterpreterParser.T__0)
                self.state = 44
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 45
                self.match(SentenceInterpreterParser.T__1)
                pass

            elif la_ == 2:
                localctx = SentenceInterpreterParser.IDIDContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(SentenceInterpreterParser.PREDICATE)
                self.state = 47
                self.match(SentenceInterpreterParser.T__0)
                self.state = 48
                self.match(SentenceInterpreterParser.ID)
                self.state = 49
                self.match(SentenceInterpreterParser.T__2)
                self.state = 50
                self.match(SentenceInterpreterParser.ID)
                self.state = 51
                self.match(SentenceInterpreterParser.T__1)
                pass

            elif la_ == 3:
                localctx = SentenceInterpreterParser.IDPContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.match(SentenceInterpreterParser.PREDICATE)
                self.state = 53
                self.match(SentenceInterpreterParser.T__0)
                self.state = 54
                self.match(SentenceInterpreterParser.ID)
                self.state = 55
                self.match(SentenceInterpreterParser.T__2)
                self.state = 56
                self.match(SentenceInterpreterParser.PREDICATE)
                self.state = 57
                self.match(SentenceInterpreterParser.T__1)
                pass

            elif la_ == 4:
                localctx = SentenceInterpreterParser.PIDContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.match(SentenceInterpreterParser.PREDICATE)
                self.state = 59
                self.match(SentenceInterpreterParser.T__0)
                self.state = 60
                self.match(SentenceInterpreterParser.PREDICATE)
                self.state = 61
                self.match(SentenceInterpreterParser.T__2)
                self.state = 62
                self.match(SentenceInterpreterParser.ID)
                self.state = 63
                self.match(SentenceInterpreterParser.T__1)
                pass

            elif la_ == 5:
                localctx = SentenceInterpreterParser.PPContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.match(SentenceInterpreterParser.PREDICATE)
                self.state = 65
                self.match(SentenceInterpreterParser.T__0)
                self.state = 66
                self.match(SentenceInterpreterParser.PREDICATE)
                self.state = 67
                self.match(SentenceInterpreterParser.T__2)
                self.state = 68
                self.match(SentenceInterpreterParser.PREDICATE)
                self.state = 69
                self.match(SentenceInterpreterParser.T__1)
                pass


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
        self._predicates[1] = self.expression__sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression__sempred(self, localctx:Expression_Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




