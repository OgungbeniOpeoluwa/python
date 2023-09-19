def credit_limit_calculator(account, balance, total_item_charged, total_credit, credit_limit):
    new_balance = balance + total_item_charged - total_credit
    if new_balance <= credit_limit:
        print("Congratulation you didnt  exceed your credit limit")
        return print(account, "=", new_balance)

    else:
        return print(f'{account:}{new_balance},\n Credit limit exceeded ')


number = int(input('Enter 1 to start calculation or press 0 to stop: '))
while number != 0:
    account_number = int(input("Enter customer account number: "))
    _balance = int(input("Enter your account balance : "))
    item_charged = int(input("enter the amount of item charged this month : "))
    _credit = int((input("Enter the total credit applied to customer account: ")))
    credit_limits = int(input("Enter credit limit of customer: "))
    credit_limit_calculator(account_number, _balance, item_charged, _credit, credit_limits)
    number = int(input('Enter 1 to start calculation or press 0 to stop: '))
