grammar MyLanguage;

// ==================== ЛЕКСИЧЕСКИЕ ПРАВИЛА ====================

// Ключевые слова
BEGIN: 'begin';
END: 'end';
ARRAY: 'array';
INTEGER: 'integer';
REAL: 'real';
BOOL: 'bool';
STRING: 'string';
LOGIC: 'logic';
FOR: 'for';
UNTIL: 'until';
DO: 'do';
IF: 'if';
THEN: 'then';
ELSE: 'else';
OR: 'or';
AND: 'and';
NOT: 'not';
OUTPUT: 'output';
GOTO: 'goto';
ENDHASH: 'end#';

// Разделители
COLON: ':';
DOLLAR: '$';
SEMICOLON: ';';
COMMA: ',';
LBRACK: '[';
RBRACK: ']';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
ASSIGN: '=';

// Операторы
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
INC: '++';
DEC: '--';
POW: '^';

// Операторы сравнения
GT: '>';
LT: '<';
GE: '>=';
LE: '<=';
NE: '!=';

// Идентификаторы
ID: [a-zA-Z][a-zA-Z0-9]*;
IDM: '_' [a-zA-Z][a-zA-Z0-9]*;
IDMET: '#' [a-zA-Z][a-zA-Z0-9]*;

// Константы
CONST_INT: [0-9]+;
CONST_REAL: [0-9]+ '.' [0-9]+;
CONST_STRING: '"' (~["\r\n])* '"';
CONST_BOOL: 'true' | 'false';

// Пробелы
WS: [ \t\r\n]+ -> skip;

// ==================== СИНТАКСИЧЕСКИЕ ПРАВИЛА ====================

program: name=ID COLON block EOF;

block: BEGIN descList=descriptionList DOLLAR stmtList=statementList END;

// Список описаний
descriptionList: first=description tail=tailDescription;

tailDescription
    : SEMICOLON next=description rest=tailDescription  # nonEmptyTail
    | /* epsilon */                                     # emptyTail
    ;

description
    : simpleVarDescription  # simpleDesc
    | arrayDescription      # arrayDesc
    ;

simpleVarDescription: varType=type vars=identifierList;

arrayDescription
    : ARRAY arrType=type arrName=IDM range=bounds     # typedArray
    | LOGIC logicName=IDM idx=index                   # logicArray
    ;

type: INTEGER | REAL | BOOL | STRING;

// Список идентификаторов
identifierList: first=ID tail=tailIdentifier;

tailIdentifier
    : COMMA next=ID rest=tailIdentifier  # nonEmptyTailId
    | /* epsilon */                      # emptyTailId
    ;

bounds: LBRACK lower=CONST_INT COLON upper=CONST_INT RBRACK;

// Список операторов
statementList: first=statement tail=tailStatement;

tailStatement
    : SEMICOLON next=statement rest=tailStatement  # nonEmptyTailStmt
    | /* epsilon */                                # emptyTailStmt
    ;

statement
    : target=variable ASSIGN expr=expression                # assignStmt
    | LBRACE body=statementList RBRACE                     # blockStmt
    | ifStmt=ifStatement                                   # ifStmt
    | outStmt=outputStatement                              # outputStmt
    | forLoop=forStatement                                 # forStmt
    | label=labelStatement                                 # labelStmt
    ;

ifStatement: IF cond=condition THEN thenBranch=statement ELSE elseBranch=statement;

outputStatement: OUTPUT LPAREN list=outputList RPAREN;

outputList: first=variable tail=tailOutput;

tailOutput
    : COMMA next=variable rest=tailOutput  # nonEmptyTailOut
    | /* epsilon */                        # emptyTailOut
    ;

forStatement: FOR loopVar=ID ASSIGN initExpr=expression SEMICOLON stepOp=step UNTIL cond=condition DO body=statement;

step: INC | DEC;

labelStatement: labelName=IDMET COLON innerStmt=statement ENDHASH;

// Переменная: простая, константа или массив
variable
    : id=ID                          # varId
    | const=constant                 # varConst
    | arr=arrayVariable              # varArray
    ;

arrayVariable: arrName=IDM (idx=index)?;

index: LBRACK element=variable RBRACK;

constant
    : intVal=CONST_INT               # constInt
    | realVal=CONST_REAL             # constReal
    | strVal=CONST_STRING            # constString
    | boolVal=CONST_BOOL             # constBool
    ;

// Выражение (ограниченная поддержка: только одна операция)
expression: base=variable tail=expressionTail;

expressionTail
    : op=(PLUS | MINUS | MULT | DIV | OR | AND | NOT | POW) 
      right=variable f=fTail       # binaryOp
    | /* epsilon */                # emptyExprTail
    ;

fTail: continuation=expression?;  // может быть пустым

condition: LPAREN left=variable op=comparisonOp right=variable RPAREN;

comparisonOp: GT | LT | GE | LE | NE | ASSIGN;