grammar Rules;

// Parser rules
root: ruleObject+ EOF;

ruleObject:
	IDENTIFIER '=' '{' nameBlock tagsBlock? conditionsBlock? '}';

nameBlock: 'name' '=' name = STRING;
tagsBlock: 'tags' '=' '{' tag = IDENTIFIER+ '}';
conditionsBlock: 'conditions' '=' '{' condition = expr+ '}';
expr:
	id = IDENTIFIER '=' (
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