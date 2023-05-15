import regex

def check_variable(tokens):
    return dec(tokens)

def dec(tokens):
    return initializer(tokens[0]) and id(tokens[1]) and new(tokens[2:-1]) and semicolon(tokens[-1])

def initializer(token):
    return token == 'ye'

def id(token):
    return token == 'car123' or token == 'apple11' or token == 'house101'

def new(tokens):
    if len(tokens) <= 3:
        return comma(tokens[0]) and id(tokens[1])
    return comma(tokens[0]) and id(tokens[1]) and new(tokens[2:]) or len(tokens[2:]) == 0

def comma(token):
    return token == ','

def semicolon(token):
    return token == ';'

print(check_variable(['ye', 'car123', ',', 'apple11', ',', 'house101', ';']))
# print(check_variable(['ye', 'car123', ';']))

