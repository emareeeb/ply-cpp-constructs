import ply.lex as lex
import ply.yacc as yacc


tokens = (
    'IDENTIFIER',   
    'TYPE',         
    'ASSIGNMENT',   
    'SEMICOLON',    
    'INTEGER',      
    'FLOAT',        
)

# Regular expressions for defined token patterns.
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

# Creating the lexer
lexer = lex.lex()

# Parser rules
def p_variable_declaration(p):
    '''variable_declaration : TYPE IDENTIFIER ASSIGNMENT expression SEMICOLON'''
    p[0] = "Valid Variable Declaration"

def p_expression(p):
    '''expression : IDENTIFIER'''
    p[0] = p[1]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Creating the parser
parser = yacc.yacc()

# Taking input from the user
input_code = input("Enter your syntax : ")

# Parsing the input and printing the result
result = parser.parse(input_code)
print(result)
