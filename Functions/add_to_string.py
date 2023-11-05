import unittest

from assignment import custom_matches


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = 'abc'
        expected = 'abcing'
        self.assertEqual(expected, custom_matches.add_to_string_function(result))

    def testIfIngIsInValue(self):
        result = "sting"
        expected = "stingly"
        self.assertEqual(expected, custom_matches.add_to_string_function(result))

    def testIfStringIsInlesserThan3(self):
        result = "it"
        expected = "it"
        self.assertEqual(expected, custom_matches.add_to_string_function(result))


if __name__ == '__main__':
    unittest.main()
