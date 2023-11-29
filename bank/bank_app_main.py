from bank.bank_app import BankApp

bank = BankApp()


def display():
    print("""
              ======================================
              1. create an account
              2  deposit
              3  withdraw
              4  transfer
              5 Check Balance
              press anything to log out
              =========================================""")
    return input("Enter a number ")


def create_account():
    name = input("Enter your first name: ")
    secondName = input("Enter your second name: ")
    pin = input("Enter your pin: ")
    result = bank.create_account(name, secondName, pin)
    print(result.display_account())
    main_menu()


def deposit():
    amount = int(input("Enter amount : "))
    accountNumber = input("Enter your account number: ")
    try:
        bank.deposit(amount, accountNumber)
        main_menu()
    except ValueError:
        main_menu()


def withdraw():
    amount = int(input("Enter amount : "))
    pin = input("Enter your pin: ")
    accountNumber = input("Enter your account number: ")
    try:
        bank.withdraw(amount, pin, accountNumber)
        main_menu()
    except ValueError as ex:
        main_menu()


def transfer():
    amount = int(input("Enter amount : "))
    pin = input("Enter your pin: ")
    accountNumber = input("Enter your account number: ")
    receiver = input("Enter reciever account number")
    try:
        bank.transfer(accountNumber, receiver, amount, pin)
        main_menu()
    except ValueError:
        main_menu()


def check_balance():
    accountNumber = input("Enter your account number: ")
    pin = input("Enter your pin: ")
    try:
        account = bank.check_balance(pin, accountNumber)
        print("Your account balance is ", account)
        main_menu()
    except ValueError:
        main_menu()


def exit_app():
    print("THANK YOU FOR BANKING WITH US")
    exit(0)


def main_menu():
    inputs = display()
    match inputs:
        case '1':
            create_account()
        case '2':
            deposit()
        case '3':
            withdraw()
        case '4':
            transfer()
        case '5':
            check_balance()
        case _:
            exit_app()


print(main_menu())
