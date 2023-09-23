user_input = int(input("Enter a binary number : "))
number = len(str(user_input))
product = 1
count = 1
while count < number:
    product *= 10
    count += 1

first_number = user_input//product
decimal_integer = first_number * 2
total = product // 10
constant = 2

while total != 0:
    divide = user_input // total % 10
    total = total // 10
    decimal_integer += divide
    decimal_integer *= constant
division = decimal_integer / 2
print(f'The Conversion of the User Binary Digit {user_input} is {division:.0f}')


