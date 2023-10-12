import unittest

from chapter4_java import tax_calculator


class MyTestCase(unittest.TestCase):
    def test_if_earnings_is_not_more_than_30000(self):
        result = 15000
        self.assertEqual(2250, tax_calculator.tax_calculator_function(result))

    def test_if_earnings_is_more_than_30000(self):
        result = 50000
        self.assertEqual(10000, tax_calculator.tax_calculator_function(result))


if __name__ == '__main__':
    unittest.main()
