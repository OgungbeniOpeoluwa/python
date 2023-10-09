import unittest
from assignment import Multiples


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Multiples.multipleTriple([3, 7, 2, 6, 5]), [27, 343, 8, 216, 125])  # add assertion here


if __name__ == '__main__':
    unittest.main()
