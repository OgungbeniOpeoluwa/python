import unittest
from unittest import TestCase

import assignment
from assignment import reverse_tuple


class MyTestCase(TestCase):
    def test_reverse_tuple(self):
        result = reverse_tuple.reverse_tuple1((10, 20, 30, 40, 50))
        expected = (50, 40, 30, 20, 10)
        self.assertEqual((50, 40, 30, 20, 10), expected)

    def test_nested_tuple(self):
        result = reverse_tuple.nested_tuple(("orange", [10, 20, 30], (5, 15, 25)), 30, 25)
        expected = ((0, 30), (1, 25))
        self.assertEqual(((0, 30), (1, 25)), expected)

    def test_unpacked_swap(self):
        result = reverse_tuple.unpacked_swapped_function((15, 25, 60, 50, 30, 40, 45, 55))
        expected = (55, 15)
        self.assertEqual((55, 15), expected)

    def test_sorting_item_by_second_item(self):
        result = reverse_tuple.sorting_by_second_item((('a', 23, 'b', 37), ('c', 11), ('d', 29)))
        expected = (('c', 11), ('a', 23), ('d', 29), ('c', 11))

    # def test_number_that_appear_more(self):
    #     result = reverse_tuple.number_appeared_more_than_once((20,10,15,20,5,30,10,35,10,40,45,5))
    #     expected = (5,10,20)

    if __name__ == '__main__':
        unittest.main()
