import unittest

from class_work import characters


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = "love"
        result2 = "evol"
        self.assertTrue(characters.equal_string(result,result2))

    def test_false(self):
        result = "love"
        result2 = "evolopt"
        self.assertFalse(characters.equal_string(result,result2))

    def test_different(self):
        result = "love"
        result2 = "biggie"
        self.assertFalse(characters.equal_string(result,result2))


if __name__ == '__main__':
    unittest.main()
