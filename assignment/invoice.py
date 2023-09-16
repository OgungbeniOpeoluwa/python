item = input("Enter name of item: ")
price = int(input("price of item :"))
credit_score = bool(input("Enter 'true' 'if credit status is good,else ignore : "))
if credit_score:
    discount = 10/100 * price
    discount_price = price - discount
    down_payment = 10 / 100 * discount_price
    print(f""""
            *******************************
            INVOICE
            *******************************
            Name of item: {item}
            Discount: {discount}
            Deposit: {down_payment}
            *******************************
            """)
else:
    down_payment_25 = 25/100 * price
    print(f""""
            *******************************
            INVOICE
            *******************************
            Name of item: {item}
            Discount: no discount
            Deposit: {down_payment_25}
            *******************************
            """)