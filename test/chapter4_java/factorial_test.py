import unittest

from chapter4_java import factorial


class MyTestCase(unittest.TestCase):
    def test_number_gives_it_factorial(self):
        result = 5
        expected = 120
        self.assertEqual(expected, factorial.factorial_function(result))  # add assertion here


if __name__ == '__main__':
    unittest.main()
