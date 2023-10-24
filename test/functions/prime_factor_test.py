import unittest

from Functions import prime_factor


class MyTestCase(unittest.TestCase):
    def test_list_of_prime_factor(self):
        number = 24
        result = [2, 2, 2, 3]
        self.assertEqual(result, prime_factor.function_of_prime(number))

    def test_list_of_prime_factor_for_5(self):
        number = 25
        result = [5, 5]
        self.assertEqual(result, prime_factor.function_of_prime(number))


if __name__ == '__main__':
    unittest.main()
