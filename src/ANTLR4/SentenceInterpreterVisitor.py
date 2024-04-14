# Generated from ./src/ANTLR4/SentenceInterpreter.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SentenceInterpreterParser import SentenceInterpreterParser
else:
    from SentenceInterpreterParser import SentenceInterpreterParser

# This class defines a complete generic visitor for a parse tree produced by SentenceInterpreterParser.

class SentenceInterpreterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SentenceInterpreterParser#Forall.
    def visitForall(self, ctx:SentenceInterpreterParser.ForallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceInterpreterParser#Exists.
    def visitExists(self, ctx:SentenceInterpreterParser.ExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceInterpreterParser#Expression.
    def visitExpression(self, ctx:SentenceInterpreterParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceInterpreterParser#Parenthesis.
    def visitParenthesis(self, ctx:SentenceInterpreterParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceInterpreterParser#Or.
    def visitOr(self, ctx:SentenceInterpreterParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceInterpreterParser#Negation.
    def visitNegation(self, ctx:SentenceInterpreterParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceInterpreterParser#And.
    def visitAnd(self, ctx:SentenceInterpreterParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceInterpreterParser#Biconditional.
    def visitBiconditional(self, ctx:SentenceInterpreterParser.BiconditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceInterpreterParser#Implication.
    def visitImplication(self, ctx:SentenceInterpreterParser.ImplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceInterpreterParser#Predicate.
    def visitPredicate(self, ctx:SentenceInterpreterParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceInterpreterParser#Uni.
    def visitUni(self, ctx:SentenceInterpreterParser.UniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceInterpreterParser#IDID.
    def visitIDID(self, ctx:SentenceInterpreterParser.IDIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceInterpreterParser#IDP.
    def visitIDP(self, ctx:SentenceInterpreterParser.IDPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceInterpreterParser#PID.
    def visitPID(self, ctx:SentenceInterpreterParser.PIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceInterpreterParser#PP.
    def visitPP(self, ctx:SentenceInterpreterParser.PPContext):
        return self.visitChildren(ctx)



del SentenceInterpreterParser