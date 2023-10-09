import unittest
from atm_card import card_validation


class MyTestCase(unittest.TestCase):
    def test_card_digit(self):
        result = card_validation.set_card_digit("123334566774214")
        self.assertEqual("123334566774214", result)

    def test_card_digit_not_more_than_13_or_16(self):
        result = card_validation.set_card_digit("12333456677")
        self.assertEqual(0, result)

    def test_length_of_card(self):
        result = card_validation.length_of_card("123334566774214")
        self.assertEqual(15, result)

    def test_first_number_of_card_is_valid(self):
        result = card_validation.check_first_number_validity("4466677887667")
        self.assertEqual("Visa Card", result)

    def test_validty_of_numbers(self):
        result = card_validation.validity_of_number("5399831619690403")
        self.assertEqual("Valid", result)


if __name__ == '__main__':
    unittest.main()
