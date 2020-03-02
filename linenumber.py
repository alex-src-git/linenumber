def is_none_or_whitespace(string):
    return not string or string.isspace()

def deduce_indentation(string):
    for (i, char) in enumerate(string):
        if (not char.isspace()):
            return i
    return 0
