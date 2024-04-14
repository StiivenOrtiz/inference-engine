from typing import List
from inference.negate import negate_sentence
from inference.clause import Clause

# def distributive(clauses):
#     for i, clause in enumerate(clauses):
#         for clause1 in clause.clauses:
#             clause2 = clause1
#             if clause2[0] == "(":
#                 clause2 = clause2[1:-1]
#             splt = clause2.split("∧")
#             if len(splt) > 1:
#                 for s in splt:
#                     new = [clause3 for clause3 in clause.clauses if clause3 != clause1]
#                     new.append(s)
#                     clauses.append(Clause(new))
#                 clauses.pop(i)

def distributive(clauses):
    index = 0
    while index < len(clauses):
        current_clause = clauses[index]
        for internal_clause in current_clause.clauses:
            clause_str = internal_clause.strip('()')
            split_clauses = clause_str.split('∧')
            if len(split_clauses) > 1:
                for part in split_clauses:
                    new_clauses = [clause for clause in current_clause.clauses if clause != internal_clause]
                    new_clauses.append(part)
                    clauses.append(Clause(new_clauses))
                clauses.pop(index)
                index -= 1
                break
        index += 1


def resolve(clause1, clause2):
    unifications = unify(clause1.clauses, clause2.clauses)
    results = []

    for unified_clauses in unifications:
        resolved_clause = set()
        has_opposite_literal = False

        for literal in unified_clauses:
            opposite_literal = negate_sentence(literal)
            if opposite_literal in unified_clauses:
                has_opposite_literal = True
            else:
                resolved_clause.add(literal)

        if has_opposite_literal:
            results.append(Clause(list(resolved_clause)))

    return results


def unify(clause1: List[str], clause2: List[str]):
    replacements = {}
    copies = []

    for c1 in clause1:
        for c2 in clause2:
            splt1 = c1.replace(")", "").replace("-", "").split("(", 1)
            splt2 = c2.replace(")", "").replace("-", "").split("(", 1)
            pred1, args1 = splt1[0], splt1[1].split(
                ",") if len(splt1) > 1 else []
            pred2, args2 = splt2[0], splt2[1].split(
                ",") if len(splt2) > 1 else []

            if pred1 == pred2:
                if len(args1) == len(args2) == 1:
                    v1, v2 = args1[0], args2[0]
                    if v1[0].isupper() and not v2[0].isupper():
                        replacements.setdefault(v2, []).append(v1)
                    elif v2[0].isupper() and not v1[0].isupper():
                        replacements.setdefault(v1, []).append(v2)
                elif len(args1) == len(args2) == 2:
                    v11, v12 = args1
                    v21, v22 = args2
                    if v11[0].isupper() and v12[0].isupper() and (
                            not v21[0].isupper()) and (not v22[0].isupper()):
                        copies.append([c.replace(v21, v11).replace(v22, v12) for c in clause1] +
                                      [c.replace(v21, v11).replace(v22, v12) for c in clause2])
                    elif (not v11[0].isupper()) and (not v12[0].isupper()) and v21[0].isupper() and v22[0].isupper():
                        copies.append([c.replace(v11, v21).replace(v12, v22) for c in clause1] +
                                      [c.replace(v11, v21).replace(v12, v22) for c in clause2])
                    elif v11[0].isupper() and (not v21[0].isupper()) and (not v22[0].isupper()):
                        replacements.setdefault(v21, []).append(v11)
                    elif (not v11[0].isupper()) and (not v12[0].isupper()) and v21[0].isupper():
                        replacements.setdefault(v11, []).append(v21)
                    elif v12[0].isupper() and (not v21[0].isupper()) and (not v22[0].isupper()):
                        replacements.setdefault(v22, []).append(v12)
                    elif (not v11[0].isupper()) and (not v12[0].isupper()) and v22[0].isupper():
                        replacements.setdefault(v12, []).append(v22)

    replace_variables(replacements, clause1 + clause2, copies)
    return copies


def replace_variables(replacements, original, copies):
    if not replacements:
        if not any(c == original for c in copies):
            copies.append(original)
    for key in replacements:
        for value in replacements[key]:
            new_clause = [c.replace(key, value) for c in original]
            new_replacements = replacements.copy()
            new_replacements.pop(key)
            replace_variables(new_replacements, new_clause, copies)
