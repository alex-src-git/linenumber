import linenumber
import unittest

class IsNoneOrWhitespaceTests(unittest.TestCase):
    def test_returns_true_when_arg_is_none(self):
        self.assertTrue(linenumber.is_none_or_whitespace(None))

    def test_returns_true_when_arg_is_empty_string(self):
        self.assertTrue(linenumber.is_none_or_whitespace(""))

    def test_returns_true_when_arg_is_whitespace(self):
        self.assertTrue(linenumber.is_none_or_whitespace("    "))

    def test_returns_false_when_arg_is_non_empty_string(self):
        self.assertFalse(linenumber.is_none_or_whitespace("Hello World"))

if __name__ == '__main__':
    unittest.main()
