import ply.lex as lex

# Special characters
special_chars = {
    '.' : 'DOT',
    '^' : 'CARET',
    '$' : 'DOLLAR',
    '*' : 'STAR',
    '+' : 'PLUS',
    '?' : 'QUESTION',
    '(' : 'LPAREN',
    ')' : 'RPAREN',
    '{' : 'LCURLY',
    '}' : 'RCURLY',
    '[' : 'LSQUARE',
    ']' : 'RSQUARE',
    '<' : 'LANGLE',
    '>' : 'RANGLE',
    ',' : 'COMMA',
    '-' : 'HYPHEN',
    '|' : 'BAR',
    '/' : 'FSLASH',
}

# Escaped chars
valid_escaped_chars = ['\\'] + list(special_chars.keys()) # Do we want to allow escaping FSLASH?

# List of token names
tokens = ['CHAR', 'DLANGLE', 'DRANGLE'] + list(special_chars.values())

# Rules
def t_DLANGLE(t):
    r'<<'
    return t

def t_DRANGLE(t):
    r'>>'
    return t

def t_escaped(t):
    r'\\.'
    if t.value[1] not in valid_escaped_chars:
        raise Exception('Invalid escape character %s' % t)
    t.type = 'CHAR'
    t.value = t.value[1]
    return t

def t_CHAR(t):
    r'.'
    if t.value == '\\':
        raise Exception('Dangling \\ at end of regular expression')
    t.type = special_chars.get(t.value, 'CHAR')
    return t

def t_error(t):
    raise Exception('Invalid input')
    
lexer = lex.lex()
