def is_none_or_whitespace(string):
    return not string or string.isspace()

def deduce_indentation(string):
    for (i, char) in enumerate(string):
        if (not char.isspace()):
            return i
    return 0

def is_more_indented(string, string_prior):
    return deduce_indentation(string) > deduce_indentation(string_prior)

def is_less_indented(string, string_prior):
    return deduce_indentation(string) < deduce_indentation(string_prior)

def prepend_line_number(number, line):
    assert not is_none_or_whitespace(line)
    return f"{number}: {line}"
