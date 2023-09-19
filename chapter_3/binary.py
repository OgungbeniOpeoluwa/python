user_input = int(input("Enter a binary number : "))
number = len(str(user_input))
product = 1
count = 1
while count < number:
    product *= 10
    count += 1

first_number = user_input//product
decimal_integer = first_number * 2
