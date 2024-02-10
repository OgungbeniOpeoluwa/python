import unittest

from assignment import count_in_character


class MyTestCase(unittest.TestCase):
    def test_something(self):
        inputs = "semicolon.africa"
        expected_result = {'s': 1, 'e': 1, 'm': 1, 'i': 2, 'c': 2, 'o': 2, 'l': 1, 'n': 1, '.': 1, 'a': 2, 'f': 1,
                           'r': 1}
        self.assertEqual(expected_result, count_in_character.returnCharacterAndCount(inputs))  # add assertion here

    def test_for_pears(self):
        inputs = "pears"
        expected_result = {'p': 1, 'e': 1, 'a': 1, 'r': 1, 's': 1}
        self.assertEqual(expected_result,count_in_character.returnCharacterAndCount(inputs))


if __name__ == '__main__':
    unittest.main()
