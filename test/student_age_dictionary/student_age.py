import unittest

from Functions import student_dictionary


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected = 25
        self.assertEqual(expected, student_dictionary.student_dictionary("ope"))

    def test_if_name_is_not_in_dictionary(self):
        expected = 50
        self.assertEqual(expected, student_dictionary.student_dictionary( "shayo", 50))


if __name__ == '__main__':
    unittest.main()
