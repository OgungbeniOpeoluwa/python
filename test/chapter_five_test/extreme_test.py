import unittest

from chapter5 import extreme


class MyTestCase(unittest.TestCase):
    def test_something(self):
        number = [2, 4, 10, 6, 7]
        self.assertEqual(12, extreme.sum_of_two_extremes(number))  # add assertion here


if __name__ == '__main__':
    unittest.main()
