import re
from getTokens import tokenize

def check_loop_declaration(tokens):
    return dec(tokens)

def dec(tokens):
    return initializer(tokens[0:2]) and cond(tokens[2:-1]) and colon(tokens[-1])

def cond(tokens):
    comp_opt = ['==', '<',">",">=", "<=","!="]
    log_opt = ['aur', 'nhi', 'ya']
    exps = []
    used_operators=[]
    k = 0
    n_exp = []
    while (k < len(tokens)):
        if tokens[k] not in log_opt:
           n_exp.append(tokens[k])
        if tokens[k] in log_opt:
            used_operators.append(tokens[k])
            exps.append(n_exp)
            n_exp=[]
        k+=1
    exps.append(n_exp)
    print(exps)

    for i in range(len(exps)):
        for j in range(len(exps[i])):
            if exps[i][len(exps[i])-1] not in comp_opt and not isValidOperator(exps[i][len(exps[i])-1]):
                if exps[i][j] in comp_opt:
                    if(not exps[i][j+1].isnumeric() and not isValidVariable(exps[i][j+1])):
                        return False
                elif j%2 == 0:
                    if(not isValidVariable(exps[i][j]) and not exps[i][j].isnumeric()):
                        return False
                else:
                    if(exps[i][j] not in comp_opt and not isValidOperator(exps[i][j])):
                        return False
            if exps[i][len(exps[i])-1] in comp_opt or isValidOperator(exps[i][len(exps[i])-1]):
                return False
                
    return True

def isValidVariable(token):
    pattern = r'^[a-zA-Z][a-zA-Z0-9]{0,18}$'
    return bool(re.match(pattern, token))

def isValidOperator(token):
    operators = ['+', '-', '*', '/', '%', '^']
    if token in operators:
        return True

def initializer(token):
    return token[0] == 'jab' and token[1] == 'tak'
    

def colon(token):
    return token == ":"

print(tokenize('jab tak num1 <= 10 :'))
print(check_loop_declaration(tokenize('jab tak num1 <= 10 :')))

print(tokenize('jab tak num1 <= 10 + :'))
print(check_loop_declaration(tokenize('jab tak num1 <= 10 + :')))

print(tokenize('jab tak num1 + num2 <= 10 aur num1 == 1 :'))
print(check_loop_declaration(tokenize('jab tak num1 + num2 <= 10 aur num1 == 1 :')))

print(tokenize('jab tak num1 + 2num2 <= 10 aur num1 == 1 :'))
print(check_loop_declaration(tokenize('jab tak num1 + 2num2 <= 10 aur num1 == 1 :')))

print(tokenize('jab tak num1 + num2 <= 10 + 2 aur num1 == 1 ya num2 == 3 :'))
print(check_loop_declaration(tokenize('jab tak num1 + num2 <= 10 + 2 aur num1 == 1 ya num2 == 3 :')))

