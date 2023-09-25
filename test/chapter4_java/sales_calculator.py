import unittest

from chapter4_java.sales_calculator import sales_calculator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sales_commission = sales_calculator(5000)
        self.assertEqual(650, sales_commission)  # add assertion here

    def test_more_than_one_unit(self):
        sales_commission = sales_calculator(5000, 4000, 3000)
        self.assertEqual(1280, sales_commission)


if __name__ == '__main__':
    unittest.main()
