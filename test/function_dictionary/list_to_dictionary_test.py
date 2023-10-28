import unittest

from function_dictionary import list_to_dictionary


class MyTestCase(unittest.TestCase):
    def test_moving_list_to_dictionary(self):
        result = ['apple', 'banana', 'coconut']
        expected = {'a': 'apple', 'b': 'banana', 'c': 'coconut'}
        self.assertEqual(expected, list_to_dictionary.function_list_to_dictionary(result))

    def test_another_word(self):
        result = ['apple', 'banana', 'coconut', 'corn']
        expected = {'a': 'apple', 'b': 'banana', 'c': 'coconut', 'C': 'corn'}
        self.assertEqual(expected, list_to_dictionary.function_list_to_dictionary(result))


if __name__ == '__main__':
    unittest.main()
