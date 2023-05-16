import re
from getTokens import tokenize

def check_variable_declaration(tokens):
    return dec(tokens)

def dec(tokens):
    # if len(tokens) >= 3:

    return initializer(tokens[0]) and id(tokens[1]) and new(tokens[2:-1]) and semicolon(tokens[-1])

def initializer(token):
    return token == 'jab tak'