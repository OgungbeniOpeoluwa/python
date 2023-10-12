import unittest

from chapter4_java import comparator


class MyTestCase(unittest.TestCase):
    def test_if_secondnumbers_is_greater(self):
        result = 10
        result2 = 12
        self.assertEqual(-1, comparator.comparator_function(result, result2))

    def test_if_FirstNumber_is_greater(self):
        result = 12
        result2 = 10
        self.assertEqual(1, comparator.comparator_function(result, result2))


if __name__ == '__main__':
    unittest.main()
