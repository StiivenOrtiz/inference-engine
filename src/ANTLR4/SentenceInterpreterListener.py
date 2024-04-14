# Generated from ./src/ANTLR4/SentenceInterpreter.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SentenceInterpreterParser import SentenceInterpreterParser
else:
    from SentenceInterpreterParser import SentenceInterpreterParser

# This class defines a complete listener for a parse tree produced by SentenceInterpreterParser.
class SentenceInterpreterListener(ParseTreeListener):

    # Enter a parse tree produced by SentenceInterpreterParser#Forall.
    def enterForall(self, ctx:SentenceInterpreterParser.ForallContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#Forall.
    def exitForall(self, ctx:SentenceInterpreterParser.ForallContext):
        pass


    # Enter a parse tree produced by SentenceInterpreterParser#Exists.
    def enterExists(self, ctx:SentenceInterpreterParser.ExistsContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#Exists.
    def exitExists(self, ctx:SentenceInterpreterParser.ExistsContext):
        pass


    # Enter a parse tree produced by SentenceInterpreterParser#Expression.
    def enterExpression(self, ctx:SentenceInterpreterParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#Expression.
    def exitExpression(self, ctx:SentenceInterpreterParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SentenceInterpreterParser#Parenthesis.
    def enterParenthesis(self, ctx:SentenceInterpreterParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#Parenthesis.
    def exitParenthesis(self, ctx:SentenceInterpreterParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by SentenceInterpreterParser#Or.
    def enterOr(self, ctx:SentenceInterpreterParser.OrContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#Or.
    def exitOr(self, ctx:SentenceInterpreterParser.OrContext):
        pass


    # Enter a parse tree produced by SentenceInterpreterParser#Negation.
    def enterNegation(self, ctx:SentenceInterpreterParser.NegationContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#Negation.
    def exitNegation(self, ctx:SentenceInterpreterParser.NegationContext):
        pass


    # Enter a parse tree produced by SentenceInterpreterParser#And.
    def enterAnd(self, ctx:SentenceInterpreterParser.AndContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#And.
    def exitAnd(self, ctx:SentenceInterpreterParser.AndContext):
        pass


    # Enter a parse tree produced by SentenceInterpreterParser#Biconditional.
    def enterBiconditional(self, ctx:SentenceInterpreterParser.BiconditionalContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#Biconditional.
    def exitBiconditional(self, ctx:SentenceInterpreterParser.BiconditionalContext):
        pass


    # Enter a parse tree produced by SentenceInterpreterParser#Implication.
    def enterImplication(self, ctx:SentenceInterpreterParser.ImplicationContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#Implication.
    def exitImplication(self, ctx:SentenceInterpreterParser.ImplicationContext):
        pass


    # Enter a parse tree produced by SentenceInterpreterParser#Predicate.
    def enterPredicate(self, ctx:SentenceInterpreterParser.PredicateContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#Predicate.
    def exitPredicate(self, ctx:SentenceInterpreterParser.PredicateContext):
        pass


    # Enter a parse tree produced by SentenceInterpreterParser#Uni.
    def enterUni(self, ctx:SentenceInterpreterParser.UniContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#Uni.
    def exitUni(self, ctx:SentenceInterpreterParser.UniContext):
        pass


    # Enter a parse tree produced by SentenceInterpreterParser#IDID.
    def enterIDID(self, ctx:SentenceInterpreterParser.IDIDContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#IDID.
    def exitIDID(self, ctx:SentenceInterpreterParser.IDIDContext):
        pass


    # Enter a parse tree produced by SentenceInterpreterParser#IDP.
    def enterIDP(self, ctx:SentenceInterpreterParser.IDPContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#IDP.
    def exitIDP(self, ctx:SentenceInterpreterParser.IDPContext):
        pass


    # Enter a parse tree produced by SentenceInterpreterParser#PID.
    def enterPID(self, ctx:SentenceInterpreterParser.PIDContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#PID.
    def exitPID(self, ctx:SentenceInterpreterParser.PIDContext):
        pass


    # Enter a parse tree produced by SentenceInterpreterParser#PP.
    def enterPP(self, ctx:SentenceInterpreterParser.PPContext):
        pass

    # Exit a parse tree produced by SentenceInterpreterParser#PP.
    def exitPP(self, ctx:SentenceInterpreterParser.PPContext):
        pass



del SentenceInterpreterParser