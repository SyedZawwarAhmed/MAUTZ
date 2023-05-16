import re
from getTokens import tokenize

var_decleared = []
assigned_var = []

def check_variable_declaration(tokens):
    valid = dec(tokens)
    if valid:
        for i in range(1, len(tokens)):
            if i%2 != 0: 
                var_decleared.append(tokens[i])
    return valid

def dec(tokens):
    if len(tokens) >= 5 and tokens[2] == "=":
        valid = initializer(tokens[0]) and id(tokens[1]) and expression(tokens[3:-1]) and semicolon(tokens[-1])
        if valid:
            assigned_var.append(tokens[1])
        return valid

    return initializer(tokens[0]) and id(tokens[1]) and new(tokens[2:-1]) and semicolon(tokens[-1])

def initializer(token):
    return token == 'ye'

def id(token):
    pattern = r'^[a-zA-Z][a-zA-Z0-9]{0,18}$'
    return bool(re.match(pattern, token))

def expression(tokens):
    operators = ['+', '-', '*', '/', '%', '^']
    valid = True
    # for item in tokens:
    #     if item
    for i in range(len(tokens)):
        if i%2 == 0:
            if tokens[i] not in assigned_var and not tokens[i].isnumeric():
                valid = False
                print(tokens[i], valid)
                # break
        else:
            if tokens[i] not in operators:
                valid = False
                print(tokens[i], valid)
                # break
        
    return valid

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

print(check_variable_declaration(['ye', 'car123', ',', 'apple11', ',', 'house1', ';']))
print(check_variable_declaration(['ye', 'car123', ';']))
print(check_variable_declaration(tokenize('ye 1a, , _b;')))
print(check_variable_declaration(tokenize('ye a, ;')))
print(check_variable_declaration(tokenize('ye 123a,b;')))
print(check_variable_declaration(tokenize('ye yeh;')))
print(check_variable_declaration(tokenize('ye a = 1;')))
print(check_variable_declaration(tokenize('ye c = a + 2 / 5;')))
print(var_decleared)
print(assigned_var)
 
