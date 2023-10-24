import unittest

from Functions import ceasre_cipher


class MyTestCase(unittest.TestCase):
    def test_arranged_letter(self):
        letter = ["V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H",
                  "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"]
        self.assertEqual(letter, ceasre_cipher.arranged_alphabet(5))

    def test_arranged_letter_key3(self):
        letter = ["X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                  "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"]
        self.assertEqual(letter, ceasre_cipher.arranged_alphabet(3))

    def test_encrypt_alphabet(self):
        letter = "H"
        expected = "E"
        self.assertEqual(expected, ceasre_cipher.encrypt(letter, 3))

    def test_encrypt_words(self):
        letter = "HELLO"
        expected = "EBIIL"
        self.assertEqual(expected, ceasre_cipher.encrypt(letter, 3))

    def test_decrypt_alphabet(self):
        letter = "E"
        expected = "H"
        self.assertEqual(expected,ceasre_cipher.decrypt(letter, 3))

    def test_dencrypt_words(self):
        letter = "EBIIL"
        expected = "HELLO"
        self.assertEqual(expected, ceasre_cipher.decrypt(letter, 3))


if __name__ == '__main__':
    unittest.main()
