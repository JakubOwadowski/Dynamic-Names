grammar Rules;

// Parser rules
root: ruleObject+ EOF;

ruleObject:
	IDENTIFIER '=' '{' nameBlock nameAdjBlock? tagsBlock? conditionsBlock? '}';

nameBlock: 'name' '=' name = STRING;
nameAdjBlock: 'name_adj' '=' name_adj = STRING;
tagsBlock: 'tags' '=' '{' tag = IDENTIFIER+ '}';
conditionsBlock: 'conditions' '=' '{' condition = expr+ '}';
expr:
	identifier = IDENTIFIER '=' (
		value = '{' expr+ '}'
		| IDENTIFIER
		| STRING
		| NUMBER
	);

// Lexer rules
IDENTIFIER: [A-Za-z][A-Za-z_0-9]*;
STRING: '"' (~["\\] | '\\' .)* '"';
NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;