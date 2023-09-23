from unittest import TestCase

from class_work.account import Account_main


class Testaccount_main(TestCase):

    def test_deposit(self):
        account_one = Account_main()
        self.assertEqual(0, account_one.get_balance())
        account_one.deposit(5000)
        self.assertEqual(5000, account_one.get_balance())

    def test_withdraw(self):
        account_one = Account_main()
        self.assertEqual(0, account_one.get_balance())
        account_one.deposit(5000)
        self.assertEqual(5000, account_one.get_balance())
        account_one.withdraw(3000)
        self.assertEqual(2000, account_one.get_balance())

    def test_deposit_negative_value(self):
        account_two = Account_main()
        self.assertEqual(0, account_two.get_balance())
        account_two.deposit(-5000)
        self.assertEqual(0, account_two.get_balance())

    def test_withdraw_more_than_amount(self):
        account_two = Account_main()
        account_two.deposit(5000)
        self.assertEqual(5000, account_two.get_balance())
        account_two.withdraw(8000)
        self.assertEqual(5000, account_two.get_balance())

    def test_transfer(self):
        account_one = Account_main()
        account_two = Account_main()
        account_one.deposit(8000)
        self.assertEqual(8000, account_one.get_balance())
        account_one.transfer(5000, account_two)
        self.assertEqual(3000, account_one.get_balance())
        self.assertEqual(5000,account_two.get_balance())