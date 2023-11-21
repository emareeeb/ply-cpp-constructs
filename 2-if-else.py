# Importing the necessary modules from the PLY (Python Lex-Yacc) library
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

# Regular expressions for token patterns
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

# Creating the lexer
lexer = lex.lex()

# Parser rules
def p_if_statement(p):
    '''
    if_statement : IF LPAREN condition RPAREN LBRACE statements RBRACE
                 | IF LPAREN condition RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE
    '''
    p[0] = "Valid if-else statement"

def p_condition(p):
    '''
    condition : expression condition
        | expression
    '''
    # Placeholder action for the condition
    pass

def p_expression(p):
    '''
    expression : IDENTIFIER
    '''
    p[0] = "Valid expression"

def p_statements(p):
    '''
    statements :  statements condition SEMICOLON
              | condition SEMICOLON
    '''
    p[0] = "Valid statements"

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Creating the parser
parser = yacc.yacc()

# Taking input from the user
input_code = input("Enter your syntax : ")

# Parsing the input and printing the result
result = parser.parse(input_code)
print(result)
