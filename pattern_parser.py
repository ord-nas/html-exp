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
    'concat : concat kstar'
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

def p_atom_open_tag(p):
    'atom : open_tag'
    p[0] = p[1]

def p_open_tag(p):
    'open_tag : LANGLE html_expression RANGLE'
    p[0] = ('OPEN-TAG', p[2])

def p_atom_close_tag(p):
    'atom : close_tag'
    p[0] = p[1]

def p_close_tag(p):
    'close_tag : LANGLE html_expression FSLASH RANGLE'
    p[0] = ('CLOSE-TAG', p[2])

#def p_atom_full_tag(p):
#    'atom : open_tag expression simple_close_tag'
#    p[0] = ('FULL-TAG', p[2])

def p_atom_simple_close_tag(p):
    'atom : LANGLE FSLASH RANGLE'
    p[0] = 'SIMPLE-CLOSE-TAG'

def p_html_expression_alt(p):
    'html_expression : html_alt'
    p[0] = p[1]

def p_html_alt_rec(p):
    'html_alt : html_alt BAR html_concat'
    p[0] = ('BAR', p[1], p[3])

def p_html_alt_base(p):
    'html_alt : html_concat'
    p[0] = p[1]

def p_html_concat_rec(p):
    'html_concat : html_concat html_kstar'
    p[0] = ('CONCAT', p[1], p[2])

def p_html_concat_base(p):
    'html_concat : html_kstar'
    p[0] = p[1]

def p_html_kstar_asterisk(p):
    'html_kstar : html_atom STAR'
    p[0] = ('KSTAR', p[1])

def p_html_kstar_atom(p):
    'html_kstar : html_atom'
    p[0] = p[1]

def p_html_atom_group(p):
    'html_atom : LPAREN html_expression RPAREN'
    p[0] = p[2]

def p_html_atom_char(p):
    'html_atom : CHAR'
    p[0] = p[1]

def p_error(p):
    print "Syntax error!"

parser = yacc.yacc()
