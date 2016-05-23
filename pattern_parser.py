import ply.yacc as yacc

from pattern_lexer import tokens

def p_expression_alt(p):
    'expression : alt'
    p[0] = p[1]

def p_alt_rec(p):
    'alt : alt BAR concat'
    p[0] = ('BAR', p[1], p[3])

def p_alt_base(p):
    'alt : concat'
    p[0] = p[1]

def p_concat_rec(p):
    'concat : kstar concat'
    p[0] = ('CONCAT', p[1], p[2])

def p_concat_base(p):
    'concat : kstar'
    p[0] = p[1]

def p_kstar_asterisk(p):
    'kstar : atom STAR'
    p[0] = ('KSTAR', p[1])

def p_kstar_atom(p):
    'kstar : atom'
    p[0] = p[1]

def p_atom_group(p):
    'atom : LPAREN expression RPAREN'
    p[0] = p[2]

def p_atom_char(p):
    'atom : CHAR'
    p[0] = p[1]

def p_error(p):
    print "Syntax error!"

parser = yacc.yacc()
