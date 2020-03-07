import linenumber
import unittest
import logging
import sys


class IsNoneOrWhitespaceTests(unittest.TestCase):
    def test_returns_true_when_arg_is_none(self):
        self.assertTrue(linenumber.is_none_or_whitespace(None))

    def test_returns_true_when_arg_is_empty_string(self):
        self.assertTrue(linenumber.is_none_or_whitespace(""))

    def test_returns_true_when_arg_is_whitespace(self):
        self.assertTrue(linenumber.is_none_or_whitespace("    "))

    def test_returns_false_when_arg_is_non_empty_string(self):
        self.assertFalse(linenumber.is_none_or_whitespace("Hello World"))


class DeduceIndentationTests(unittest.TestCase):
    def test_returns_0_when_arg_is_empty_string(self):
        self.assertEqual(0, linenumber.deduce_indentation(""))

    def test_returns_0_when_arg_is_whitespace(self):
        self.assertEqual(0, linenumber.deduce_indentation("    "))

    def test_returns_indentation_when_arg_is_indented_string(self):
        self.assertEqual(4, linenumber.deduce_indentation("    :"))

    def test_raises_type_error_when_arg_is_none(self):
        with self.assertRaises(TypeError):
            linenumber.deduce_indentation(None)


class IsLessIndentedTests(unittest.TestCase):
    def test_returns_false_when_strings_have_equal_indentation(self):
        self.assertFalse(linenumber.is_less_indented("  a", "  b"))

    def test_returns_false_when_string_prior_is_less_indented(self):
        self.assertFalse(linenumber.is_less_indented("   a,", " b"))

    def test_returns_true_when_string_prior_is_more_indented(self):
        self.assertTrue(linenumber.is_less_indented(" a", "   b"))

    def test_raises_type_error_when_arg_0_is_none(self):
        with self.assertRaises(TypeError):
            linenumber.is_less_indented(None, "")

    def test_raises_type_error_when_arg_1_is_none(self):
        with self.assertRaises(TypeError):
            linenumber.is_less_indented("", None)


class IsMoreIndentedTests(unittest.TestCase):
    def test_returns_false_when_strings_have_equal_indentation(self):
        self.assertFalse(linenumber.is_more_indented("  a", "  b"))

    def test_returns_true_when_string_prior_is_less_indented(self):
        self.assertTrue(linenumber.is_more_indented("   a,", " b"))

    def test_returns_false_when_string_prior_is_more_indented(self):
        self.assertFalse(linenumber.is_more_indented(" a", "   b"))

    def test_raises_type_error_when_arg_0_is_none(self):
        with self.assertRaises(TypeError):
            linenumber.is_more_indented(None, "")

    def test_raises_type_error_when_arg_1_is_none(self):
        with self.assertRaises(TypeError):
            linenumber.is_more_indented("", None)


class PairWiseTests(unittest.TestCase):
    def test_returns_elements_n_and_n_minus_1_in_loop(self):
        elements = range(100)
        i = 0
        for (prior, current) in linenumber.pairwise(elements):
            i += 1
            self.assertNotEqual(current, prior)
            self.assertEqual(elements[i], current)
            self.assertEqual(elements[i - 1], prior)


class PrependLineNumberTests(unittest.TestCase):
    def test_returns_string_longer_than_line_arg(self):
        string = "Hello World"
        string_returned = linenumber.prepend_line_number(0, string)
        self.assertGreater(len(string_returned), len(string))

    def test_returns_string_that_contains_line_arg(self):
        string = "Hello World"
        string_returned = linenumber.prepend_line_number(0, string)
        self.assertIn(string, string_returned)

    def test_returns_string_that_contains_number_arg(self):
        string = "Hello World"
        string_returned = linenumber.prepend_line_number(42, string)
        self.assertIn("42", string_returned)

    def test_returns_string_that_is_not_equal_to_line_arg(self):
        string = "Hello World"
        string_returned = linenumber.prepend_line_number(0, string)
        self.assertNotEqual(string, string_returned)


class PrependLineNumbersTests(unittest.TestCase):
    def test_returns_string_longer_than_input_arg(self):
        def count_chars(string_list):
            return len("".join(string_list))
        lines = ["Hello", "World", "Or", "Something", "Idk"]
        lines_returned = list(linenumber.prepend_line_numbers(lines))
        self.assertGreaterEqual(count_chars(lines_returned), count_chars(lines))

    def test_returns_same_number_of_lines_as_inputted(self):
        lines = ["What", "Are", "Those", "?!!"]
        lines_returned = list(linenumber.prepend_line_numbers(lines))
        self.assertEqual(len(lines), len(lines_returned))

    def test_returns_lines_that_contain_input(self):
        lines = ["Hello", "Is", "This", "Thing", "On", "???"]
        lines_returned = list(linenumber.prepend_line_numbers(lines))
        lines_returned_joined = "".join(lines)
        for line_inputted in lines:
            self.assertIn(line_inputted, lines_returned_joined)

    def test_returns_lines_in_same_order_as_input(self):
        lines = ["Hey", "That's", "Pretty", "Good"]
        lines_returned = list(linenumber.prepend_line_numbers(lines))
        for i, line_inputted in enumerate(lines):
            self.assertIn(line_inputted, lines_returned[i])


class NumericPrefixTests(unittest.TestCase):
    def test_constructor_assigns_numbers(self):
        numbers = [1, 4, 5, 3]
        prefix = linenumber.NumericPrefix(numbers)
        self.assertEqual(numbers, prefix.numbers)

    def test_constructor_without_numbers_argument_assigns_new_list(self):
        prefix = linenumber.NumericPrefix()
        self.assertIsNotNone(prefix.numbers)
        self.assertEqual(1, len(prefix.numbers))

    def test_str_returns_string(self):
        prefix = linenumber.NumericPrefix()
        string = str(prefix)
        self.assertIsNotNone(string)

    def test_str_returns_string_that_is_not_empty_or_whitespace(self):
        prefix = linenumber.NumericPrefix()
        string = str(prefix)
        self.assertTrue(string)
        self.assertFalse(string.isspace())

    def test_str_returns_string_greater_equal_number_list(self):
        numbers = [1, 3, 4000, 5, 100]
        numbers_len = len("".join(map(str, numbers)))
        prefix = linenumber.NumericPrefix(numbers)
        string = str(prefix)
        self.assertGreaterEqual(len(string), numbers_len)

    def test_increment_increments_last_number(self):
        prefix = linenumber.NumericPrefix()
        prefix.increment()
        self.assertEqual(2, prefix.numbers[-1])

    def test_increment_increments_last_number_only(self):
        prefix = linenumber.NumericPrefix([1534, 435, 32])
        prefix.increment()
        self.assertEqual(33, prefix.numbers[2])
        self.assertEqual(435, prefix.numbers[1])
        self.assertEqual(1534, prefix.numbers[0])

    def test_indent_increases_list_len_by_1(self):
        prefix = linenumber.NumericPrefix()
        prefix.indent()
        self.assertEqual(2, len(prefix.numbers))

    def test_un_indent_reduces_list_len_by_1(self):
        numbers = [1]
        prefix = linenumber.NumericPrefix(numbers)
        prefix.indent()
        prefix.indent()
        prefix.indent()
        prefix.un_indent()
        self.assertEqual(3, len(prefix.numbers))


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main()
