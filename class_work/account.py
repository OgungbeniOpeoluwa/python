class Account_main:

    def __init__(self):
        self._balance = 0

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount

    def transfer(self, amount):
        self.withdraw(amount)
        name.self.deposit(amount)

