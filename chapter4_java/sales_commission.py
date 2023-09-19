number = int(input("press 1 to start your sales commission or 0 to quit: "))

while number != 0:
    goods = input("Enter the name of your company: ")
    number_of_item_sold = int(input("Enter the  number of goods sold for the week: "))
    total = 0
    if number_of_item_sold < 1:
        item = float(input("enter the price of the item: "))
        total += item
    else:
        for user_input in range(number_of_item_sold):
            item = float(input("kindly enter price of each goods : "))
            total += item
    constant = 200
    percent = (9/100) * total
    gain = constant + percent
    print(f'{goods}, your sales earning for the week = {gain}')
    number = int(input("press 1 to start your sales commission or 0 to quit: "))
