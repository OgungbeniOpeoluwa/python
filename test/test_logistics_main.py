import unittest

from java_python import logistics_main
from java_python.logistics_main import rider_calculator


class MyTestCase(unittest.TestCase):
    def test_delivery_lesser_than_50(self):
        payment = rider_calculator(25)
        self.assertEqual(payment, 9000)  # add assertion here

    def test_within_50(self):
        wage = rider_calculator(50)
        self.assertEqual(wage, 15000)

    def test_within_60(self):
        wage = rider_calculator(68)
        self.assertEqual(wage, 22000)

    def test_greater_than_70(self):
        wage = rider_calculator(80)
        self.assertEqual(wage, 45000)


if __name__ == '__main__':
    unittest.main()
