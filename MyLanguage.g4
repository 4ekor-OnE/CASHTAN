grammar MyLanguage;

// ==================== ЛЕКСИЧЕСКИЕ ПРАВИЛА ====================

// Ключевые слова (должны быть перед ID)
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

// Операторы сравнения (O в BNF: >, <, =, ==)
GT: '>';
LT: '<';
EQ: '==';  // == для сравнения
// ASSIGN уже определен как '='

// Идентификаторы
// id: буква (буква|цифра)*
ID: [a-zA-Z][a-zA-Z0-9]*;

// idm: _ буква (буква|цифра)*
IDM: '_' [a-zA-Z][a-zA-Z0-9]*;

// Idmet: # буква (буква|цифра)*
IDMET: '#' [a-zA-Z][a-zA-Z0-9]*;

// Константы (C в BNF)
// C: цифра+ | цифра+.цифра+ | "строка"
CONST_INT: [0-9]+;
CONST_REAL: [0-9]+ '.' [0-9]+;
CONST_STRING: '"' (~["\r\n])* '"';

// Пробелы
WS: [ \t\r\n]+ -> skip;

// ==================== СИНТАКСИЧЕСКИЕ ПРАВИЛА ====================

// <Программа>::= <имя программы> : <блок>
program: name=ID COLON block EOF;

// <блок>::= begin <список описаний> $ <список операторов> end
block: BEGIN descList=descriptionList DOLLAR stmtList=statementList END;

// <список описаний>::= <описание> <хвост описания>
descriptionList: first=description tail=tailDescription;

// <хвост описания>::= ; <описание> <хвост описания>
// <хвост описания>::= & (пусто)
tailDescription
    : SEMICOLON next=description rest=tailDescription  # nonEmptyTail
    | /* epsilon */                                     # emptyTail
    ;

// <описание>::= <описание простых переменных>
// <описание>::= <описание массивов>
description
    : simpleVarDescription  # simpleDesc
    | arrayDescription      # arrayDesc
    ;

// <описание простых переменных>::= <вид> <список идентификаторов>
simpleVarDescription: varType=type vars=identifierList;

// <описание массивов>::= array <вид> <имя массива> <границы>
// <описание массивов>::= logic <имя массива> <индекс>
arrayDescription
    : ARRAY arrType=type arrName=IDM range=bounds     # typedArray
    | LOGIC logicName=IDM idx=index                   # logicArray
    ;

// <вид>::= integer | real | bool | string
type: INTEGER | REAL | BOOL | STRING;

// <список идентификаторов>::= id <хвост идентификаторов>
identifierList: first=ID tail=tailIdentifier;

// <хвост идентификаторов>::= , id <хвост идентификаторов>
// <хвост идентификаторов>::= & (пусто)
tailIdentifier
    : COMMA next=ID rest=tailIdentifier  # nonEmptyTailId
    | /* epsilon */                      # emptyTailId
    ;

// <границы>::= [ C : C ]
bounds: LBRACK lower=CONST_INT COLON upper=CONST_INT RBRACK;

// <список операторов>::= <оператор> <хвост операторов>
statementList: first=statement tail=tailStatement;

// <хвост операторов>::= ; <оператор> <хвост операторов>
// <хвост операторов>::= & (пусто)
tailStatement
    : SEMICOLON next=statement rest=tailStatement  # nonEmptyTailStmt
    | /* epsilon */                                # emptyTailStmt
    ;

// <оператор>::= <переменная> = <выражение>
// <оператор>::= { <список операторов> }
// <оператор>::= <условный>
// <оператор>::= <ввод>
// <оператор>::= <цикл>
// <оператор>::= <метка>
// <оператор>::= <условие> (из BNF)
statement
    : target=variable ASSIGN expr=expression                # assignStmt
    | LBRACE body=statementList RBRACE                     # blockStmt
    | ifStmt=ifStatement                                   # ifStmt
    | outStmt=outputStatement                              # outputStmt
    | forLoop=forStatement                                 # forStmt
    | label=labelStatement                                 # labelStmt
    | cond=condition                                       # conditionStmt
    ;

// <условный>::= if <условие> then <оператор> else <оператор>
ifStatement: IF cond=condition THEN thenBranch=statement ELSE elseBranch=statement;

// <ввод>::= output ( <список вывода> )
outputStatement: OUTPUT LPAREN list=outputList RPAREN;

// <список вывода>::= <переменная> <список вывода_хвост>
outputList: first=variable tail=tailOutput;

// <список вывода_хвост>::= , <переменная> <список вывода_хвост>
// <список вывода_хвост>::= & (пусто)
tailOutput
    : COMMA next=variable rest=tailOutput  # nonEmptyTailOut
    | /* epsilon */                        # emptyTailOut
    ;

// <цикл>::= for <переменная> = <начальное_значение> ; <шаг> until <условие> do <тело цикла>
forStatement: FOR loopVar=variable ASSIGN initVal=constant SEMICOLON stepOp=step UNTIL cond=condition DO body=loopBody;

// <начальное_значение>::= C (константа)
// Уже определено в constant

// <шаг>::= ++ | --
step: INC | DEC;

// <тело цикла>::= <оператор>
// <тело цикла>::= goto <имя метки>
loopBody
    : stmt=statement                    # loopBodyStmt
    | GOTO labelName=IDMET              # loopBodyGoto
    ;

// <метка>::= <имя метки> : <оператор> end#
labelStatement: labelName=IDMET COLON innerStmt=statement ENDHASH;

// <переменная>::= id | C | <переменная_массив>
variable
    : id=ID                          # varId
    | const=constant                 # varConst
    | arr=arrayVariable              # varArray
    ;

// <переменная_массив>::= idm <индекс>
arrayVariable: arrName=IDM idx=index;

// <индекс>::= [ <переменная> ] | & (пусто)
index
    : LBRACK element=variable RBRACK  # indexWithVar
    | /* epsilon */                   # indexEmpty
    ;

// Константы
constant
    : intVal=CONST_INT               # constInt
    | realVal=CONST_REAL             # constReal
    | strVal=CONST_STRING            # constString
    ;

// <выражение>::= <переменная> <выражение_хвост>
expression: base=variable tail=expressionTail;

// <выражение_хвост>::= + <переменная><F_хвост>
// <выражение_хвост>::= - <переменная><F_хвост>
// <выражение_хвост>::= * <переменная><F_хвост>
// <выражение_хвост>::= / <переменная><F_хвост>
// <выражение_хвост>::= or <переменная><F_хвост>
// <выражение_хвост>::= and <переменная><F_хвост>
// <выражение_хвост>::= not <переменная><F_хвост>
// <выражение_хвост>::= ^ <переменная><F_хвост>
// <выражение_хвост>::= & (пусто)
expressionTail
    : op=(PLUS | MINUS | MULT | DIV | OR | AND | NOT | POW)
      right=variable f=fTail          # binaryOp
    | /* epsilon */                   # emptyExprTail
    ;

// <F_хвост>::= <выражение>
// <F_хвост>::= & (пусто)
fTail
    : continuation=expression         # fTailExpr
    | /* epsilon */                   # fTailEmpty
    ;

// <условие>::= ( <переменная> O <переменная> )
condition: LPAREN left=variable op=comparisonOp right=variable RPAREN;

// O: >, <, =, ==
comparisonOp: GT | LT | ASSIGN | EQ;
