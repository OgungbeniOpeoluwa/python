item_price = int(input("Enter the price of the product : "))
user_input = int(input("Enter amount paid for the item bought : "))

quarter = 25
dime = 10
nickel = 5
pennies = 1

quarter_count = 0
dime_count = 0
nickel_count = 0
pennies_count = 0

if user_input > item_price:
    total = user_input - item_price
    cents = total / 100
    while cents != 0:
        if cents >= quarter:
            cents -= quarter
            quarter_count += 1
        elif quarter > cents >= dime:
            cents -= dime
            dime_count += 1
        elif dime > cents >= nickel:
            cents -= nickel
            nickel_count += 1
        else:
            cents -= pennies
            pennies_count += 1
print(f'your change is{quarter_count}quarter,{dime_count}dimes,{nickel_count}nickle,{pennies_count}pennie')

