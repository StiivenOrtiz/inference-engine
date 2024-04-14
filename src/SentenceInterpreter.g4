grammar SentenceInterpreter;

/* Rules */
sentencia:
	ALL ID sentencia		# Forall
	| EXISTS ID sentencia	# Exists
	| expression_			# Expression;

expression_:
	expression_ BICONDITIONAL expression_	# Biconditional
	| expression_ IMPLICATION expression_	# Implication
	| '(' expression_ ')'					# Parenthesis
	| expression_ AND expression_			# And
	| expression_ OR expression_			# Or
	| NOT expression_						# Negation
	| predicate_							# Predicate;

predicate_:
	PREDICATE '(' op = (ID | PREDICATE) ')'		# Uni
	| PREDICATE '(' ID ',' ID ')'				# IDID
	| PREDICATE '(' ID ',' PREDICATE ')'		# IDP
	| PREDICATE '(' PREDICATE ',' ID ')'		# PID
	| PREDICATE '(' PREDICATE ',' PREDICATE ')'	# PP;

/* Tokens */
ALL: '∀' | '/all';
EXISTS: '∃' | '/exists';
IMPLICATION: '=>';
BICONDITIONAL: '<=>';
OR: '∨' | '/or';
AND: '∧' | '/and';
NOT: '-';
ID: [a-z];
PREDICATE: [A-Z][a-zA-Z]*;

/* Ignored whitespace */
IGNORED: [ \t\n\r]+ -> skip;