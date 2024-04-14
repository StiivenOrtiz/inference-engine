def negate_sentence(sentence):
    """
    Negates a logical sentence expressed in propositional logic.

    The function takes a sentence in the form of a conjunction of
    disjunctions (using '∧' and '∨' respectively) and returns the
    negated sentence in the form of a disjunction of conjunctions.

    Parameters:
        sentence (str): A string representing the logical sentence.

    Returns:
        str: The negated sentence as a disjunction of conjunctions.
    """

    conjunction_parts = sentence.replace(" ", "").split("∧")
    negated_parts = []

    for part in conjunction_parts:

        disjunction_parts = part.split("∨")
        negated_disjunction = []

        for subpart in disjunction_parts:

            negated_subpart = "-" + subpart
            negated_subpart = negated_subpart.replace("-(", "(-")
            negated_disjunction.append(negated_subpart)

        negated_conjunction = "∧".join(negated_disjunction)
        negated_parts.append(negated_conjunction)

    return "∨".join(negated_parts).replace("--", "")
