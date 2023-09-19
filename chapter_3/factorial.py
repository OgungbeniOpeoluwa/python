user_input = int(input("Enter a non_negative integer: "))
while user_input < 0:
    user_input = int(input("Enter a non_negative integer: "))

product = 1

while user_input >= 1:
    product *= user_input
    user_input -= 1

print(product)
