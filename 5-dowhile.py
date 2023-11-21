# Importing the necessary modules from the PLY (Python Lex-Yacc) library
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

# Regular expressions for token patterns
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
# t_DO = r'do'  # Uncomment this line to enable the 'do' token
# t_WHILE = r'while'  # Uncomment this line to enable the 'while' token
t_ignore = r' '

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

# Creating the lexer
lexer = lex.lex()

# Parser rules
def p_do_while_loop(p):
    '''do_while_loop : DO LBRACE statements RBRACE WHILE LPAREN condition RPAREN SEMICOLON'''
    p[0] = "Valid do-while statement"

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

# Creating the parser
parser = yacc.yacc()

# Taking input from the user
input_code = '''do {
    x = x - 1;
} while (x > 0);
'''

input_code = input("Enter your syntax : ")
result = parser.parse(input_code)
print(result)
