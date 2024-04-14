from typing import List

from inference.negate import negate_sentence


class Clause:
    def __init__(self, clauses):
        self.clauses = clauses
        self.solution = []


# Add a new clause to the list of clauses
def add_clause(clauses, new_clause):
    clauses.append(new_clause)


def is_null_clause(clauses: List[Clause]):
    literals = set()
    for clause in clauses:
        if len(clause.clauses) == 1:
            literal = clause.clauses[0]
            negated_literal = negate_sentence(literal)
            if negated_literal in literals:
                return True
            literals.add(literal)
    return False


def there_are_clauses_to_resolve(clauses):
    return any(len(c.clauses) <= 1 and len(c.solution)
               < len(clauses) - 1 for c in clauses)


def find_clauses_to_resolve(clauses: List[Clause]):
    for i, clause1 in enumerate(clauses):
        for j, clause2 in enumerate(clauses):
            if i != j and clause2 not in clause1.solution:
                clause1.solution.append(clause2)
                clause2.solution.append(clause1)
                if any(clause1_literal.split("(", 1)[0] == negate_sentence(clause2_literal.split("(", 1)[
                       0]) for clause1_literal in clause1.clauses for clause2_literal in clause2.clauses):
                    return clause1, clause2
    return Clause([]), Clause([])
