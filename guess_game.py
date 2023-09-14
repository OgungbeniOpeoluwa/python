import random

number = int(input("Enter a number between 1 and 10"))
number2 = random.randint(1, 10)
print(number2)
if number == number2:
    print("you guessed correctly")

while number != number2:
    number = int(input("Enter a number between 1 and 10"))
    number2 = random.randint(1, 10)

    if number == number2:
        print("you guessed correctly")
