# PES2UG22CS093 - Areeb Ahmed - B Section
# PES2UG22CS080 - Ansh T Shetty - B Section

# AFLL MINI PROJECT 
# Language : C++ Constructs
# (1)Variable-Declaration, (2)If-Else, (3)While loop, (4)For loop, (5)Do-While loop.

# NOTE : All the 5 Constructs are in this same file, for execution separate file or commenting methods could be used. 

# 1 : Variable-Declaration  --------------------------------------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'IDENTIFIER',
    'TYPE',
    'ASSIGNMENT',
    'SEMICOLON',
    'INTEGER',
    'FLOAT',
)

t_SEMICOLON = r';'
t_ignore = r' '

def t_TYPE(t):
    r'\b(int|char|float|double)\b'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z0-9._><\-][a-zA-Z0-9._><\-]*'
    t.type = 'IDENTIFIER'
    return t

def t_ASSIGNMENT(t):
    r'='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
def p_variable_declaration(p):
    '''variable_declaration : TYPE IDENTIFIER ASSIGNMENT expression SEMICOLON'''
    p[0] = "Valid Variable Declaration"

def p_expression(p):
    '''expression : IDENTIFIER'''
    p[0] = p[1]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

input_code = input("Enter your syntax : ")
result = parser.parse(input_code)
print(result)


# 2 : IF ELSE  --------------------------------------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'IF',
    'ELSE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'IDENTIFIER',
)

#t_IF = r'if'
# t_ELSE = r'else'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_ignore = r' '

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t
def t_IDENTIFIER(t):
    r'[a-zA-Z0-9_><=\-+][a-zA-Z0-9_><=\-+]*'
    t.type = 'IDENTIFIER'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser


def p_if_statement(p):
    '''
    if_statement : IF LPAREN condition RPAREN LBRACE statements RBRACE
                 | IF LPAREN condition RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE
    '''
    p[0]= "Valid if else statement"



def p_condition(p):
    '''
    condition : expression condition
        | expression
    '''
    

def p_expression(p):
    '''
    expression : IDENTIFIER
    '''
    p[0]= "Valid if else statement"




def p_statements(p):
    '''
    statements :  statements condition SEMICOLON
              | condition SEMICOLON
    '''
    p[0]= "Valid if else statement"
        

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

# Test the parser
input_code = '''
if (x > 0) {
    x = x - 1;
} else {
    x = x + 1;
}
'''

input_code = input("Enter your syntax : ")
result = parser.parse(input_code)
print(result)

# 3 : WHILE  --------------------------------------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'IDENTIFIER',
    'LPAREN',
    'RPAREN',
    'WHILE',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
# t_WHILE = r'while'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_ignore = r' '

def t_WHILE(t):
    r'while'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z0-9_><=\-][a-zA-Z0-9_><=\-]*'
    t.type = 'IDENTIFIER'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
def p_while_loop(p):
    '''while_loop : WHILE LPAREN condition RPAREN LBRACE statements RBRACE'''
    p[0]= "Valid while statement"

def p_condition(p):
    '''condition : condition IDENTIFIER
        | IDENTIFIER'''
    if len(p)==3:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_statements(p):
    '''statements : statement statements
                  | statement'''
    p[0]= "Valid if else statement"

def p_statement(p):
    '''statement : while_loop
                 | condition SEMICOLON'''
    if len(p) == 2:
        p[0] = p[1]
    else :
        p[0] = p[2]

# def p_expression(p):
#     '''expression : IDENTIFIER'''
#     p[0] = ('identifier', p[1])

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()


# Test the parser
input_code = '''while (x > 0) {
    x = x - 1;
    while(x==0)
    {
        x=5;
    }
}
'''
# lexer.input(input_code)
# for i in lexer:
#     print(i)

input_code = input("Enter your syntax : ")
result = parser.parse(input_code)
print(result)

# 4 : FOR  --------------------------------------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'IDENTIFIER',
    'LPAREN',
    'RPAREN',
    'FOR',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_ignore = r' '

def t_FOR(t):
    r'for'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z0-9_><=+\-\/][a-zA-Z0-9_><=\-+\/]*'
    t.type = 'IDENTIFIER'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
def p_for_loop(p):
    '''for_loop : FOR LPAREN condition SEMICOLON condition SEMICOLON condition RPAREN LBRACE statements RBRACE'''
    p[0]= "Valid for statement"

def p_for_init(p):
    '''for_init : condition SEMICOLON
                | SEMICOLON'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_for_update(p):
    '''for_update : condition SEMICOLON
                  | SEMICOLON'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_statements(p):
    '''statements : statement statements
                  | statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_statement(p):
    '''statement : for_loop
                 | condition SEMICOLON'''
    if len(p) == 2:
        p[0] = p[1]


    else:
        p[0] = p[1]

def p_condition(p):
    '''condition : condition IDENTIFIER
        | IDENTIFIER'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

# Test the parser
input_code = '''for (int i = 0; i < 10; ++i) {
    sfkjvskjvj;
}
'''
# lexer.input(input_code)
# for i in lexer:
#     print(i)
input_code = input("Enter your syntax : ")
result = parser.parse(input_code)
print(result)

# 5 : DO WHILE  --------------------------------------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'IDENTIFIER',
    'LPAREN',
    'RPAREN',
    'WHILE',
    'DO',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
# t_DO = r'do'
# t_WHILE = r'while'
t_ignore=r' '

def t_DO(t):
    r'do'
    return t

def t_WHILE(t):
    r'while'
    return t
def t_IDENTIFIER(t):
    r'[a-zA-Z0-9_><=\-][a-zA-Z0-9_><=\-]*'
    t.type = 'IDENTIFIER'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
def p_do_while_loop(p):
    '''do_while_loop : DO LBRACE statements RBRACE WHILE LPAREN condition RPAREN SEMICOLON'''
    p[0]= "Valid do while statement"

def p_condition(p):
    '''condition : condition IDENTIFIER
                 | IDENTIFIER'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_statements(p):
    '''statements : statement statements
                  | statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_statement(p):
    '''statement : do_while_loop
                 | condition SEMICOLON'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

# Test the parser
input_code = '''do {
    x = x - 1;
} while (x > 0);
'''
lexer.input(input_code)
for i in lexer:
    print(i)

input_code = input("Enter your syntax : ")
result = parser.parse(input_code)
print(result)
