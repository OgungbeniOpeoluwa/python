import unittest

from assignment import check_leapYear


class MyTestCase(unittest.TestCase):
    def test_something(self):
        number = 1800
        self.assertFalse(check_leapYear.isleapYear(number))

    def test_is_a_leap_year(self):
        number = 2400
        self.assertTrue(check_leapYear.isleapYear(number))


if __name__ == '__main__':
    unittest.main()
