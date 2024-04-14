from antlr4 import CommonTokenStream, InputStream
from ANTLR4.SentenceInterpreterLexer import SentenceInterpreterLexer
from ANTLR4.SentenceInterpreterParser import SentenceInterpreterParser
from ANTLR4.SentenceInterpreterVisitor import SentenceInterpreterVisitor

from .negate import negate_sentence
from inference.clause import Clause, add_clause, is_null_clause, there_are_clauses_to_resolve, find_clauses_to_resolve
from inference.resolution import distributive, resolve


def refutation(axioms, sentence):
    add_axiom(axioms, negate_sentence(sentence))
    fnc = conjunctive_normal_form(axioms)
    clauses = [Clause(a.split("∨")) for a in fnc]
    distributive(clauses)
    while there_are_clauses_to_resolve(clauses):
        clause1, clause2 = find_clauses_to_resolve(clauses)
        results = resolve(clause1, clause2)

        for result in results:
            if len(result.clauses) > 0 and not any(
                    c.clauses == result.clauses for c in clauses):
                add_clause(clauses, result)
                clauses = sorted(clauses, key=lambda c: len(c.clauses))
        if is_null_clause(clauses):
            return True
    return False

# Agregar una sentence a la lista de axioms.


def add_axiom(axioms, sentence):
    axioms.append(sentence)

def conjunctive_normal_form(axioms):
    count = 1
    axioms_n = []
    for i in range(0, len(axioms)):
        ap = visit(axioms[i])
        ap = ap.replace("#", str(i + 1))
        n_ap = ap.split("/bicond")
        for n in n_ap:
            print(f"{count}. {n}")
            count += 1
            if n[0] == "(":
                n = n[1:-1]
            axioms_n.append(n)
    return axioms_n


def visit(axioma):
    axioma_n = axioma.replace('∀',
                              '/all').replace('∃',
                                              '/exists').replace('∧',
                                                                 '/and').replace('∨',
                                                                                 '/or')
    visitor = SentenceInterpreterVisitor()
    fnc = visitor.visit(
        SentenceInterpreterParser(
            CommonTokenStream(
                SentenceInterpreterLexer(
                    InputStream(axioma_n)))).sentencia())
    return fnc
