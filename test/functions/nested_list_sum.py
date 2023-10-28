import unittest

from Functions import nested_list


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = [[2, 4, 5, 6], [2, 3, 5, 6]]
        expected = 33
        self.assertEqual(expected, nested_list.sum_list2(result))


if __name__ == '__main__':
    unittest.main()
