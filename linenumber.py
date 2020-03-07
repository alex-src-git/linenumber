from itertools import tee


def is_none_or_whitespace(string):
    return not string or string.isspace()


def deduce_indentation(string):
    for (i, char) in enumerate(string):
        if not char.isspace():
            return i
    return 0


def is_more_indented(string, string_prior):
    return deduce_indentation(string) > deduce_indentation(string_prior)


def is_less_indented(string, string_prior):
    return deduce_indentation(string) < deduce_indentation(string_prior)


def prepend_line_number(number, line):
    assert not is_none_or_whitespace(line)
    return f"{number}: {line}"


def pairwise(iterable):
    prior, current = tee(iterable)
    next(current, None)
    return zip(prior, current)


class NumericPrefix():
    def __init__(self, numbers=None):
        if numbers is None:
            self.numbers = [1]
        else:
            self.numbers = numbers

    def __str__(self):
        return ".".join(map(str, self.numbers))

    def increment(self):
        self.numbers[-1] += 1

    def indent(self):
        self.numbers.append(1)

    def un_indent(self):
        self.numbers.pop()
        self.increment()
