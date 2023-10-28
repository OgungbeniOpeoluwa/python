import unittest

from Functions import unique_even_number


class MyTestCase(unittest.TestCase):
    def test_something(self):
        number = [1, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 6, 12, 15, 10, 4, 6, 14]
        expected = {2, 4, 6, 8, 10, 12, 14}
        self.assertEqual(expected,unique_even_number.unique_numbers(number))  # add assertion here


if __name__ == '__main__':
    unittest.main()
