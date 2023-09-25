from chapter4_java.sales_calculator import sales_calculator

number = int(input("press 1 to start your sales commission or 0 to quit: "))

while number != 0:
    goods = input("Enter the name of your company: ")
    number_of_item_sold = int(input("Enter the  number of goods sold for the week: "))
    total = 0
    result = 0
    if number_of_item_sold == 1:
        item = float(input("enter the price of the item: "))
        total = sales_calculator(item)
    else:
        for user_input in range(number_of_item_sold):
            item = float(input("kindly enter price of each goods : "))
            result += item
        total = sales_calculator(result)
    print(f'{goods}, your sales earning for the week = {total}')
    number = int(input("press 1 to start your sales commission or 0 to quit: "))
