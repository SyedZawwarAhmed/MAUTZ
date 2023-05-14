def tokenize(string):
    tokens = []
    token = ''
    for character in string:
        if character == ' '   or character == '\n':
            tokens.append(token)
            token = ''
        else:
            if character == '\t'or character == ';' or character == ',':
                tokens.append(token)
                tokens.append(character)
                token = ''
            else:
                token += character
    tokens.append(token)
    return list(filter(lambda x: x != '', tokens))