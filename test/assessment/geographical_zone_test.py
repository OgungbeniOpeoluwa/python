import unittest

from assignment import geographical_zone


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = geographical_zone
        number = "Kaduna"
        expected = "NORTHWEST"
        self.assertEqual(expected, geographical_zone.find_state(number))  # add assertion here


if __name__ == '__main__':
    unittest.main()
