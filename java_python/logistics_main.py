def rider_calculator(delivery_amount):
    if delivery_amount < 50:
        total = delivery_amount * 160 + 5000

    elif delivery_amount <= 59:
        total = delivery_amount * 200 + 5000

    elif delivery_amount <= 69:
        total = delivery_amount * 250 + 5000

    else:
        total = delivery_amount * 500 + 5000
    return total


number = int(input("Enter total number of delivery package: "))
wage = rider_calculator(number)
print("your wage for today is : ", wage)
