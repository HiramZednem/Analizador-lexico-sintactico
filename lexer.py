# lexer.py
import re

def lexical_analysis(code):
    tokens = []
    token_specification = [
        ('FOR', r'\bfor\b'),
        ('INT', r'\bint\b'),
        ('PRINTLN', r'\bprintln\b'),
        ('SYSTEM', r'\bsystem\.out\.println\b'),
        ('PARENIZQ', r'\('),
        ('PARENDER', r'\)'),
        ('LLAVEIZQ', r'\{'),
        ('LLAVEDER', r'\}'),
        ('PUNTOCOMA', r';'),
        ('NUM', r'\d+'),
        ('ID', r'[A-Za-z_]\w*'),
        ('OP', r'\+\+|\-\-|\+|\-|\<=|\>=|\<|\>|\==|\!=|\&\&|\|\|'),
        ('EQ', r'='),
        ('STRING', r'".*"'),
        ('COMA', r','),
        ('SPACE', r'\s+'),
        ('UNKNOWN', r'.')
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'SPACE':
            continue
        tokens.append((kind, value, line_num, column))
    return tokens
