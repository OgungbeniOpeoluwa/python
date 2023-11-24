import unittest

from assessment.chapter5 import Teephone_word_generator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        number = "6862377"
        result = "NUMBERS"
        print(Teephone_word_generator.wordGeneratorFunction(number))
        self.assertEqual(result, Teephone_word_generator.wordGeneratorFunction(number))  # add assertion here


if __name__ == '__main__':
    unittest.main()
