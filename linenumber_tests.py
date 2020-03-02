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

if __name__ == '__main__':
    unittest.main()
