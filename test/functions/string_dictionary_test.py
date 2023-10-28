import unittest

from assignment import string_dictionary


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected = {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
        self.assertEqual(expected, string_dictionary.return_string_in_dictionary("google.com"))

    def test_another_something(self):
        expected = {'o': 1, 'p': 1, 'e': 1}
        self.assertEqual(expected, string_dictionary.return_string_in_dictionary("ope"))


if __name__ == '__main__':
    unittest.main()
