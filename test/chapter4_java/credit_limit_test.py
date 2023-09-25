import unittest

import chapter4_java
from chapter4_java.credit_limit import credit_limit_calculator


class MyTestCase(unittest.TestCase):
    def test_account_name(self):
        number = credit_limit_calculator(787, 5000, 3000, 2000, 10000)
        self.assertEqual(number, 6000)  # add assertion here

    def test_exceed_limit(self):
        balance = credit_limit_calculator(546, 10000, 8000, 12000, 5000)
        self.assertEqual(balance, 6000)


if __name__ == '__main__':
    unittest.main()
