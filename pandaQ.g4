grammar pandaQ;

// Definición de reglas
instruction: (plot | assignment | query) SEMICOLON;

plot: PLOT tableName;

assignment: ID ASSIG query;

query: statement (ORDER BY orderByExpressionList)?;

statement: SELECT (selectItem (COMMA selectItem)*) FROM tableSource (WHERE condition)?;

selectItem: STAR                                #selectItemStar
          | columnNameList                      #selectItemColumnNameList
          | expression AS columnName            #selectItemAS
          ;

expression: NUMBER                              #expressionNumber
          | expression STAR expression          #expressionAritmetic
          | expression DIV expression           #expressionAritmetic
          | expression PLUS expression          #expressionAritmetic
          | expression MINUS expression         #expressionAritmetic
          | columnName                          #expressionColumnName
          ;

columnNameList: columnName (COMMA columnName)*;

columnName: ID;

tableSource: tableName (INNER JOIN tableName ON condition)*;

tableName: ID;

orderByExpressionList: orderByExpression (COMMA orderByExpression)*;

orderByExpression: columnName (ASC | DESC)?;

condition: booleanExpression                    #conditionBoolean
        | columnName EQUAL columnName           #conditionEqual
        | columnName IN LPAREN query RPAREN     #conditionIn
        ;

booleanExpression: booleanTerm (OR booleanTerm)*;

booleanTerm: booleanFactor (AND booleanFactor)*;

booleanFactor: NOT? booleanPrimary;

booleanPrimary: '(' booleanExpression ')'       #booleanPrimaryBoolean
             | comparisonExpression             #booleanPrimaryComparison
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
INNER: [Ii][Nn][Nn][Ee][Rr];
JOIN: [Jj][Oo][Ii][Nn];
ON: [Oo][Nn];
PLOT: [Pp][Ll][Oo][Tt];
IN: [Ii][Nn];
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
ASSIG: ':=';
// Ignorar espacios en blanco y saltos de línea
WS: [ \t\r\n]+ -> skip;
