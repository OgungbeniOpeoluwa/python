import unittest

from assessment import subsequence_array


class MyTestCase(unittest.TestCase):
    def test_something(self):
        parent_list = [4, 5, -8, 0, 1, 7, 6]
        sub_list = [9, 0, 7]
        self.assertTrue(subsequence_array.validate_subsequence(parent_list, sub_list))


if __name__ == '__main__':
    unittest.main()
