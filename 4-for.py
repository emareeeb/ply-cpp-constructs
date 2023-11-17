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
    p[0] = (p[1],p[2],p[4],p[6],p[8],p[9],p[11])

# def p_for_init(p):
#     '''for_init : condition SEMICOLON
#                 | SEMICOLON'''
#     if len(p) == 3:
#         p[0] = p[2]
#     else:
#         p[0] = p[1]

# def p_for_update(p):
#     '''for_update : condition SEMICOLON
#                   | SEMICOLON'''
#     if len(p) == 3:
#         p[0] = p[2]
#     else:
#         p[0] = p[1]

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
lexer.input(input_code)
for i in lexer:
    print(i)

result = parser.parse(input_code)
print(result)
