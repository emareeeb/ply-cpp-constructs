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
