#chosen language -c++
#constructs:-
#1.variable declaration
#2.if-else
#3.while loop
#4.for loop
#5.do-while loop

#  TO RUN THE CODE UNCOMMENT EACH LINE BY REMOVING # SYMBOL(ONLY ONE) 

#       -------------------------------------------1.variable declaration--------------------------------------------------        #


# import ply.lex as lex
# import ply.yacc as yacc

# # Lexer
# tokens = (
#     'IDENTIFIER',
#     'TYPE',
#     'ASSIGNMENT',
#     'SEMICOLON',
#     'INTEGER',
#     'FLOAT',
# )

# # t_TYPE = r''
# # t_ASSIGNMENT = r'='
# t_SEMICOLON = r';'
# t_ignore = r' '

# def t_TYPE(t):
#     r'int\s| char | float | double'
#     return t

# def t_IDENTIFIER(t):
#     r'[a-zA-Z0-9._><\-][a-zA-Z0-9._><\-]*'
#     t.type = 'IDENTIFIER'
#     return t
# def t_ASSIGNMENT(t):
#     r'='
#     return t

# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += t.value.count('\n')

# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)


# lexer = lex.lex()

# # Parser
# def p_variable_declaration(p):
#     '''variable_declaration : TYPE IDENTIFIER ASSIGNMENT expression SEMICOLON'''
#     p[0] = (p[1], p[2], p[3], p[5])

# # def  p_type(p):
# #     ''' type: INTEGER
# #               FLOAT'''
        
# def p_expression(p):
#     '''expression : IDENTIFIER'''
                   
#     p[0] = p[1]

# def p_error(p):
#     print(f"Syntax error at '{p.value}'")

# parser = yacc.yacc()

# # Test the parser
# input_code = '''float x=5.5;'''
# lexer.input(input_code)

# for i in lexer:
#     print(i)

# result = parser.parse(input_code)
# print(result)

#       --------------------------------------------------------------------------------------------------------------------------------        #

#       -----------------------------------------------------2.if-else------------------------------------------------------------------        #

# import ply.lex as lex
# import ply.yacc as yacc

# # Lexer
# tokens = (
#     'IF',
#     'ELSE',
#     'LPAREN',
#     'RPAREN',
#     'LBRACE',
#     'RBRACE',
#     'SEMICOLON',
#     'IDENTIFIER',
# )

# #t_IF = r'if'
# # t_ELSE = r'else'
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_LBRACE = r'\{'
# t_RBRACE = r'\}'
# t_SEMICOLON = r';'
# t_ignore = r' '

# def t_IF(t):
#     r'if'
#     return t

# def t_ELSE(t):
#     r'else'
#     return t
# def t_IDENTIFIER(t):
#     r'[a-zA-Z0-9_><=\-+][a-zA-Z0-9_><=\-+]*'
#     t.type = 'IDENTIFIER'
#     return t




# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += t.value.count('\n')

# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# lexer = lex.lex()

# # Parser


# def p_if_statement(p):
#     '''
#     if_statement : IF LPAREN condition RPAREN LBRACE statements RBRACE
#                  | IF LPAREN condition RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE
#     '''
#     if len(p)==7:
#         p[0]=(p[1],p[2],p[4],p[5],p[7])
#     else :
#         p[0]=(p[1],p[2],p[4],p[5],p[7],p[8],p[9],p[11])



# def p_condition(p):
#     '''
#     condition : expression condition
#         | expression
#     '''
#     if len(p)==3:
#         p[0]=[p[1]]+p[2]
#     else:
#         p[0]=[p[1]]

# def p_expression(p):
#     '''
#     expression : IDENTIFIER
#     '''



# def p_statements(p):
#     '''
#     statements :  statements condition SEMICOLON
#               | condition SEMICOLON
#     '''
#     if len(p)==3:
#         p[0]=([p[1]],p[2])

#     else:
#         p[0]=([p[1]],[p[2]],p[3])
        

# def p_error(p):
#     print(f"Syntax error at '{p.value}'")

# parser = yacc.yacc()

# # Test the parser
# input_code = '''
# if (x > 0) {
#     x = x - 1;
# } else {
#     x = x + 1;
# }
# '''

# lexer.input(input_code)

# for token in lexer:
#     print(token)

# result = parser.parse(input_code)
# print(result)


# #       ----------------------------------------------------------------------------------------------------------------        #

# #       ---------------------------------------------3.while-loop-------------------------------------------------------        #

# import ply.lex as lex
# import ply.yacc as yacc

# # Lexer
# tokens = (
#     'IDENTIFIER',
#     'LPAREN',
#     'RPAREN',
#     'WHILE',
#     'LBRACE',
#     'RBRACE',
#     'SEMICOLON',
# )

# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# # t_WHILE = r'while'
# t_LBRACE = r'\{'
# t_RBRACE = r'\}'
# t_SEMICOLON = r';'
# t_ignore = r' '

# def t_WHILE(t):
#     r'while'
#     return t

# def t_IDENTIFIER(t):
#     r'[a-zA-Z0-9_><=\-][a-zA-Z0-9_><=\-]*'
#     t.type = 'IDENTIFIER'
#     return t

# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += t.value.count('\n')

# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# lexer = lex.lex()

# # Parser
# def p_while_loop(p):
#     '''while_loop : WHILE LPAREN condition RPAREN LBRACE statements RBRACE'''
#     p[0] = ( p[1], p[2],p[4],p[5],p[7])

# def p_condition(p):
#     '''condition : condition IDENTIFIER
#         | IDENTIFIER'''
#     if len(p)==3:
#         p[0] = p[2]
#     else:
#         p[0] = p[1]

# def p_statements(p):
#     '''statements : statement statements
#                   | statement'''
#     if len(p) == 2:
#         p[0] = [p[1]]
#     else:
#         p[0] = [p[1]] + p[2]

# def p_statement(p):
#     '''statement : while_loop
#                  | condition SEMICOLON'''
#     if len(p) == 2:
#         p[0] = p[1]
#     else :
#         p[0] = p[2]

# # def p_expression(p):
# #     '''expression : IDENTIFIER'''
# #     p[0] = ('identifier', p[1])

# def p_error(p):
#     print(f"Syntax error at '{p.value}'")

# parser = yacc.yacc()


# # Test the parser
# input_code = '''while (x > 0) {
#     x = x - 1;
#     while(x==0)
#     {
#         x=5;
#     }
# }
# '''
# lexer.input(input_code)
# for i in lexer:
#     print(i)


# result = parser.parse(input_code)
# print(result)


#       --------------------------------------------------------------------------------------------------      #

#       ----------------------------------------4.for-loop------------------------------------------------      #

# import ply.lex as lex
# import ply.yacc as yacc

# # Lexer
# tokens = (
#     'IDENTIFIER',
#     'LPAREN',
#     'RPAREN',
#     'FOR',
#     'LBRACE',
#     'RBRACE',
#     'SEMICOLON',
# )

# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_LBRACE = r'\{'
# t_RBRACE = r'\}'
# t_SEMICOLON = r';'
# t_ignore = r' '

# def t_FOR(t):
#     r'for'
#     return t

# def t_IDENTIFIER(t):
#     r'[a-zA-Z0-9_><=+\-\/][a-zA-Z0-9_><=\-+\/]*'
#     t.type = 'IDENTIFIER'
#     return t

# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += t.value.count('\n')

# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# lexer = lex.lex()

# # Parser
# def p_for_loop(p):
#     '''for_loop : FOR LPAREN condition SEMICOLON condition SEMICOLON condition RPAREN LBRACE statements RBRACE'''
#     p[0] = (p[1],p[2],p[4],p[6],p[8],p[9],p[11])

# # def p_for_init(p):
# #     '''for_init : condition SEMICOLON
# #                 | SEMICOLON'''
# #     if len(p) == 3:
# #         p[0] = p[2]
# #     else:
# #         p[0] = p[1]

# # def p_for_update(p):
# #     '''for_update : condition SEMICOLON
# #                   | SEMICOLON'''
# #     if len(p) == 3:
# #         p[0] = p[2]
# #     else:
# #         p[0] = p[1]

# def p_statements(p):
#     '''statements : statement statements
#                   | statement'''
#     if len(p) == 2:
#         p[0] = [p[1]]
#     else:
#         p[0] = [p[1]] + p[2]

# def p_statement(p):
#     '''statement : for_loop
#                  | condition SEMICOLON'''
#     if len(p) == 2:
#         p[0] = p[1]
#     else:
#         p[0] = p[1]

# def p_condition(p):
#     '''condition : condition IDENTIFIER
#         | IDENTIFIER'''
#     if len(p) == 3:
#         p[0] = p[2]
#     else:
#         p[0] = p[1]

# def p_error(p):
#     print(f"Syntax error at '{p.value}'")

# parser = yacc.yacc()

# # Test the parser
# input_code = '''for (int i = 0; i < 10; ++i) {
#     sfkjvskjvj;
# }
# '''
# lexer.input(input_code)
# for i in lexer:
#     print(i)

# result = parser.parse(input_code)
# print(result)

#       ---------------------------------------------------------------------------------------------       #
#       ------------------------------------------5.do-while-----------------------------------------       #

# import ply.lex as lex
# import ply.yacc as yacc

# # Lexer
# tokens = (
#     'IDENTIFIER',
#     'LPAREN',
#     'RPAREN',
#     'WHILE',
#     'DO',
#     'LBRACE',
#     'RBRACE',
#     'SEMICOLON',
# )

# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_LBRACE = r'\{'
# t_RBRACE = r'\}'
# t_SEMICOLON = r';'
# # t_DO = r'do'
# # t_WHILE = r'while'
# t_ignore=r' '

# def t_DO(t):
#     r'do'
#     return t

# def t_WHILE(t):
#     r'while'
#     return t
# def t_IDENTIFIER(t):
#     r'[a-zA-Z0-9_><=\-][a-zA-Z0-9_><=\-]*'
#     t.type = 'IDENTIFIER'
#     return t

# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += t.value.count('\n')

# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# lexer = lex.lex()

# # Parser
# def p_do_while_loop(p):
#     '''do_while_loop : DO LBRACE statements RBRACE WHILE LPAREN condition RPAREN SEMICOLON'''
#     p[0] = (p[1],p[2],p[4],p[5],p[6],p[8],p[9])

# def p_condition(p):
#     '''condition : condition IDENTIFIER
#                  | IDENTIFIER'''
#     if len(p) == 3:
#         p[0] = p[2]
#     else:
#         p[0] = p[1]

# def p_statements(p):
#     '''statements : statement statements
#                   | statement'''
#     if len(p) == 2:
#         p[0] = [p[1]]
#     else:
#         p[0] = [p[1]] + p[2]

# def p_statement(p):
#     '''statement : do_while_loop
#                  | condition SEMICOLON'''
#     if len(p) == 2:
#         p[0] = p[1]
#     else:
#         p[0] = p[2]

# def p_error(p):
#     print(f"Syntax error at '{p.value}'")

# parser = yacc.yacc()

# # Test the parser
# input_code = '''do {
#     x = x - 1;
# } while (x > 0);
# '''
# lexer.input(input_code)
# for i in lexer:
#     print(i)

# result = parser.parse(input_code)
# print(result)

#       ----------------------------------------------------------------------------------------------------        #