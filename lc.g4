grammar lc;

// Definición de reglas
query: statement (ORDER BY orderByExpressionList)? SEMICOLON;

statement: SELECT (selectItem (COMMA selectItem)*) FROM tableName;

selectItem: STAR
          | columnNameList
          | expression AS columnName
          ;

expression: NUMBER
          | expression STAR expression
          | expression DIV expression
          | expression PLUS expression
          | expression MINUS expression
          | columnName
          ;

columnNameList: columnName (COMMA columnName)*;

columnName: ID;

tableName: ID;

orderByExpressionList: orderByExpression (COMMA orderByExpression)*;

orderByExpression: columnName (ASC | DESC)?;

// Tokens
SELECT: 'SELECT';
FROM: 'FROM';
AS: 'AS';
ORDER: 'ORDER';
BY: 'BY';
ASC: 'ASC';
DESC: 'DESC';
STAR: '*';
COMMA: ',';
SEMICOLON: ';';
LPAREN: '(';
RPAREN: ')';
DIV: '/';
PLUS: '+';
MINUS: '-';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+('.'[0-9]+)?; 
// Ignorar espacios en blanco y saltos de línea
WS: [ \t\r\n]+ -> skip;
