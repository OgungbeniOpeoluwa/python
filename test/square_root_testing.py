import unittest

from class_work.square_root import square_root


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = square_root(25)
        self.assertEqual(5, result)

    def test_for_negative_number(self):
        result = square_root(-25)
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
