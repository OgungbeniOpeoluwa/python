from unittest import TestCase

from assignment import funtion_list


class Test(TestCase):
    def test_largest_element(self):
        numbers = funtion_list.largest_element([5, 2, 3, 4, 10, 4])
        self.assertEqual(10, numbers)

    def test_reverse(self):
        numbers = funtion_list.reverse([1, 2, 3, 4, 5, 7])
        self.assertEqual([7, 5, 4, 3, 2, 1], numbers)

    def test_if_an_element_occurs(self):
        result = funtion_list.element_occurs([1, 2, 3, 4, 5], 6)
        self.assertEqual(False, result)

    def test_element_oddly_position(self):
        result = funtion_list.oddly_place([10, 32, 5, 6, 7, 8, 9])
        self.assertEqual([10, 5, 7, 9], result)

    def test_even_position(self):
        result = funtion_list.even_place([10, 32, 5, 4, 6, 7, 8])
        self.assertEqual([32, 4, 7], result)

    def test_running_total(self):
        result = funtion_list.running_total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(55, result)

    def test_String_To_palindrome(self):
        result = funtion_list.palindrome("damola")
        self.assertEqual(False, result)

    def test_cocainating_two_list(self):
        result = funtion_list.cocatinating_two_list(["a", "b", "c", "d"], [1, 2, 3, 4, ])
        self.assertEqual(["a", "b", "c", "d", 1, 2, 3, 4], result)

    def test_cocatinating_in_between(self):
        result = funtion_list.cocatinating_in_between(["a", "b", "c", "d"], [1, 2, 3, 4, 5, 7])
        self.assertEqual(["a", 1, "b", 2, "c", 3, "d", 4, 5, 7], result)

    def test_number_to_list(self):
        result = funtion_list.digit_to_list(2, 3, 4, 5, 6, 8, 9)
        self.assertEqual([2, 3, 4, 5, 6, 8, 9], result)

    def test_sum_of_digit(self):
        result = funtion_list.sums_forloop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(55, result)

    def test_sum_of_digit2(self):
        result = funtion_list.sums_whileloop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(55, result)
