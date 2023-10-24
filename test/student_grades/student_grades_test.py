from assignment import student_grade
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = [[67,21,49],[98,62,56],[93,34,27]]
        self.assertEqual(227, student_grade.total(result,))


if __name__ == '__main__':
    unittest.main()
