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
