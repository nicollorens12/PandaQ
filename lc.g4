grammar lc;

// Definición de reglas
query: statement SEMICOLON;

statement: SELECT (STAR | columnNameList) FROM tableName;

columnNameList: columnName (COMMA columnName)*;

columnName: ID;

tableName: ID;

// Tokens
SELECT: 'SELECT';
FROM: 'FROM';
STAR: '*';
COMMA: ',';
SEMICOLON: ';';
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Ignorar espacios en blanco y saltos de línea
WS: [ \t\r\n]+ -> skip;
