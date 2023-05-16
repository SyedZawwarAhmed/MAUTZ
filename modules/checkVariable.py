import re
from getTokens import tokenize

def check_variable_declaration(tokens):
    return dec(tokens)

def dec(tokens):
    # if len(tokens) >= 3:

    return initializer(tokens[0]) and id(tokens[1]) and new(tokens[2:-1]) and semicolon(tokens[-1])

def initializer(token):
    return token == 'ye'

def id(token):
    pattern = r'^[a-zA-Z][a-zA-Z0-9]{0,18}$'
    return bool(re.match(pattern, token))

def new(tokens):
    if len(tokens) == 0:
        return True
    if len(tokens) < 2:
        return False
    if len(tokens) == 2:
        return comma(tokens[0]) and id(tokens[1])
    return comma(tokens[0]) and id(tokens[1]) and new(tokens[2:]) or len(tokens[2:]) == 0

def comma(token):
    return token == ','

def semicolon(token):
    return token == ';'

# print(check_variable(['ye', 'car123', ',', 'apple11', ',', 'house1', ';']))
# print(check_variable(['ye', 'car123', ';']))
# print(check_variable(tokenize('ye 1a, , _b;')))
# print(check_variable(tokenize('ye a, ;')))
# print(check_variable(tokenize('ye 123a,b;')))
# print(check_variable(tokenize('ye yeh;')))
# print(check_variable(tokenize('ye ;')))