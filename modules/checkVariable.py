import re
from getTokens import tokenize

declared_variables = []
assigned_variables = []


def check_variable_declaration(tokens):
    valid = dec(tokens)
    return valid


def dec(tokens):
    if len(tokens) >= 5 and tokens[2] == "=":
        valid = initializer(tokens[0]) and id(tokens[1]) and expression(
            tokens[3:-1]) and semicolon(tokens[-1])
        if valid:
            assigned_variables.append(tokens[1])
            declared_variables.append(tokens[1])
        return valid

    if len(tokens) >= 4 and tokens[1] == "=":
        valid = is_declared(tokens[0]) and expression(
            tokens[2:-1]) and semicolon(tokens[-1])
        if valid:
            assigned_variables.append(tokens[0])
            declared_variables.append(tokens[0])
        return valid

    valid = initializer(tokens[0]) and id(tokens[1]) and new(tokens[2:-1]) and semicolon(tokens[-1])
    if valid:
        for i in range(1, len(tokens)):
            if i % 2 != 0:
                declared_variables.append(tokens[i])
    return valid


def initializer(token):
    return token == 'ye'


def id(token):
    pattern = r'^[a-zA-Z][a-zA-Z0-9]{0,18}$'
    return bool(re.match(pattern, token))


def expression(tokens):
    operators = ['+', '-', '*', '/', '%', '^']
    valid = True
    for i in range(len(tokens)):
        if i % 2 == 0:
            if tokens[i] not in assigned_variables and not tokens[i].isnumeric() and not tokens[i][0] == "'" and not tokens[i][-1]:
                valid = False
                break
        else:
            if tokens[i] not in operators:
                valid = False
                break

    return valid


def is_declared(variable):
    return variable in assigned_variables or variable in declared_variables


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


print(check_variable_declaration(
    ['ye', 'car123', ',', 'apple11', ',', 'house1', ';']))
print(check_variable_declaration(['ye', 'car123', ';']))
print(check_variable_declaration(tokenize('ye 1a, , _b;')))
print(check_variable_declaration(tokenize('ye a, ;')))
print(check_variable_declaration(tokenize('ye 123a,b;')))
print(check_variable_declaration(tokenize('ye yeh;')))
print(check_variable_declaration(tokenize("ye a = 'hello';")))
print(check_variable_declaration(tokenize("ye c = a + 2 / 5 - 'hello';")))
print(check_variable_declaration(tokenize("ye c;")))
print(check_variable_declaration(tokenize("c = a + 2 / 7;")))
print(declared_variables)
print(assigned_variables)


# print(check_variable(['ye', 'car123', ',', 'apple11', ',', 'house1', ';']))
# print(check_variable(['ye', 'car123', ';']))
# print(check_variable(tokenize('ye 1a, , _b;')))
# print(check_variable(tokenize('ye a, ;')))
# print(check_variable(tokenize('ye 123a,b;')))
# print(check_variable(tokenize('ye yeh;')))
# print(check_variable(tokenize('ye ;')))
