import unittest

from chapter5 import panlindrome


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = "radar"
        self.assertTrue(panlindrome.is_pandlidrome(result))

    def test_String_is_not_a_pandlindrome(self):
        result = "mowe"
        self.assertFalse(panlindrome.is_pandlidrome(result))

    def test_Another_String_is_A_pandlindrome(self):
        result = "11211"
        self.assertTrue(panlindrome.is_pandlidrome(result))



if __name__ == '__main__':
    unittest.main()
