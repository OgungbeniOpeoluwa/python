import unittest
from unittest import TestCase

import assignment
from assignment import reverse_tuple


class MyTestCase(TestCase):
    def test_reverse_tuple(self):
        result = (10, 20, 30, 40, 50)
        expected = (50, 40, 30, 20, 10)
        self.assertEqual(expected, reverse_tuple.reverse_tuple1(result))

    def test_nested_tuple(self):
        expected = ((0, 30), (1, 25))
        self.assertEqual(expected, reverse_tuple.nested_tuple(("orange", [10, 20, 30], (5, 15, 25)), 30, 25))

    def test_unpacked_swap(self):
        result = (15, 25, 60, 50, 30, 40, 45, 55)
        expected = (55, 15)
        self.assertEqual(expected, reverse_tuple.unpacked_swapped_function(result))

    def test_sorting_item_by_second_item(self):
        result = (('a', 23, 'b', 37), ('c', 11), ('d', 29))
        expected = (('c', 11), ('a', 23), ('d', 29), ('c', 11))
        self.assertEqual(expected, reverse_tuple.sorting_by_second_item(result))

    if __name__ == '__main__':
        unittest.main()
