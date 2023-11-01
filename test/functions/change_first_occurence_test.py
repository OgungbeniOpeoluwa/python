import unittest

from assessment import change_first_occurence


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = "restart"
        replace = '$'
        letter = 'r'
        expected = "resta$t"
        self.assertEqual(expected, change_first_occurence.change_first_occurrence_function(result, letter, replace))

    def test_another_letter(self):
        result = "letter"
        replace = '$'
        letter = 't'
        expected = "let$er"
        self.assertEqual(expected, change_first_occurence.change_first_occurrence_function(result, letter, replace))


if __name__ == '__main__':
    unittest.main()
