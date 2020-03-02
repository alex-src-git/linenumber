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

class PrependLineNumber(unittest.TestCase):
    def test_raises_assertion_error_when_line_arg_is_none(self):
        with self.assertRaises(AssertionError):
            linenumber.prepend_line_number(0, None)

    def test_raises_assertion_error_when_line_arg_is_empty_string(self):
        with self.assertRaises(AssertionError):
            linenumber.prepend_line_number(0, "")

    def test_raises_assertion_error_when_line_arg_is_whitespace(self):
        with self.assertRaises(AssertionError):
            linenumber.prepend_line_number(0, "    ")

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

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main()
