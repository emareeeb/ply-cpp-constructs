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
