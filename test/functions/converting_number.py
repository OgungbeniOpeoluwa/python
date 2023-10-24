import unittest

from Functions import coverting_number


class MyTestCase(unittest.TestCase):
    def test_decimal_to_binary(self):
        number = 34
        self.assertEqual("100010", coverting_number.decimal_to_binary(number))

    def test_binary_to_binary(self):
        number = 101
        self.assertEqual(5, coverting_number.binary_to_decimal(number))


if __name__ == '__main__':
    unittest.main()
