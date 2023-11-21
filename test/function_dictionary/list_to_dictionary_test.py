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

    def test_taking_two_list_and_return_dictionary(self):
        result1 = ['a', 'b', 'c', 'd', 'e']
        result2 = [1, 2, 3, 4, 5]
        result = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(result, list_to_dictionary.two_list_to_dictionary(result1, result2))

    def test_something(self):
        result = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        self.assertEqual(70, list_to_dictionary.difference_in_list(result))

    def test_removing_multiple_string(self):
        results = [",'ABC','xyz',", 'abc', 'XYZ']
        expected = ['ABC', 'xyz', 'abc', 'XYZ']
        self.assertEqual(expected, list_to_dictionary.remove_multiple_string_function(results))

    def test_remove_duplicate_numbers_base_on_value_given(self):
        result = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
        expect = [1, 2, 5]
        self.assertEqual(expect, list_to_dictionary.remove_duplicate_numbers_function(result, 2))

    def test_remove_duplicate_another_numbers_base_on_value_given(self):
        result = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
        expect = [1, 2, 3, 5]
        self.assertEqual(expect, list_to_dictionary.remove_duplicate_numbers_function(result, 1))

    def test_split_items(self):
        result = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        expected = [10, 75, 20, 30, 15], [5, 40, 25, 40, 35]
        self.assertEqual(expected, list_to_dictionary.split_list_function(result))

    def test_if_list_is_not_the_same_length(self):
        result = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35, 45]
        expected = [10, 75, 20, 30, 15], [5, 40, 25, 40, 35, 45]
        self.assertEqual(expected, list_to_dictionary.split_list_function(result))


if __name__ == '__main__':
    unittest.main()