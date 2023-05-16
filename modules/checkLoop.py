import re
from getTokens import tokenize

def check_loop_declaration(tokens):
    return dec(tokens)

def dec(tokens):
    return initializer(tokens[0:2]) and cond(tokens[2:-1]) and colon(tokens[-1])

def cond(tokens):
    comp_opt = ['==', '<',">",">=", "<=","!="]
    exp1 = []
    for i in range(len(tokens)):
       if tokens[i] not in comp_opt:
           exp1.append(tokens[i])
       else:
           opt = tokens[i]
           exp2 = tokens[i+1:]

    return exp(exp1) and opt != '' and exp(exp2)

def exp(tokens):
    operators = ['+', '-', '*', '/', '%', '^']
    lo
    if len(tokens) == 1:
        # check if the var is assigned and return that var
    

def initializer(token):
    return token == 'jab tak'

def colon(token):
    return token == ';'
print(tokenize('jab tak num1 + num2 <= 10 aur num1 == 1 :'))

# <loop> → jab tak <cond> : <body>
# <cond> → <exp> <cmp_op> <exp> <NEW> | nahi var1 <NEW>
# <NEW> → ya <cond> | aur <cond> |Ω
# <exp> → var1<NEXT>
# <NEXT> → <mth_op>var2 | Ω
# < cmp_op> → ==, <,>,>=, <=, 