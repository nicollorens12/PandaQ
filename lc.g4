grammar lc;

// Definición de reglas
query: statement (ORDER BY orderByExpressionList)? SEMICOLON;

statement: SELECT (selectItem (COMMA selectItem)*) FROM tableName (WHERE condition)?;

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

condition: booleanExpression;

booleanExpression: booleanTerm (OR booleanTerm)*;

booleanTerm: booleanFactor (AND booleanFactor)*;

booleanFactor: NOT? booleanPrimary;

booleanPrimary: '(' booleanExpression ')'
             | comparisonExpression
             ;

comparisonExpression: columnName (EQUAL | NOT_EQUAL | LESS | LESS_OR_EQUAL | GREATER | GREATER_OR_EQUAL) (NUMBER | TRUE | FALSE | STRING);

// Tokens
SELECT: [Ss][Ee][Ll][Ee][Cc][Tt];
FROM: [Ff][Rr][Oo][Mm];
AS: [Aa][Ss];
ORDER: [Oo][Rr][Dd][Ee][Rr];
BY: [Bb][Yy];
ASC: [Aa][Ss][Cc];
DESC: [Dd][Ee][Ss][Cc];
WHERE: [Ww][Hh][Ee][Rr][Ee];
OR: [Oo][Rr];
AND: [Aa][Nn][Dd];
NOT: [Nn][Oo][Tt];
STAR: '*';
COMMA: ',';
SEMICOLON: ';';
LPAREN: '(';
RPAREN: ')';
DIV: '/';
PLUS: '+';
MINUS: '-';
EQUAL: '=';
NOT_EQUAL: '<>';
LESS: '<';
LESS_OR_EQUAL: '<=';
GREATER: '>';
GREATER_OR_EQUAL: '>=';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+('.'[0-9]+)?;
STRING: '\'' ~'\''* '\'';
TRUE: [Tt][Rr][Uu][Ee];
FALSE: [Ff][Aa][Ll][Ss][Ee];
// Ignorar espacios en blanco y saltos de línea
WS: [ \t\r\n]+ -> skip;
