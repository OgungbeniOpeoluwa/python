import random

user_input = int(input("Enter a number within 0 and 6"))
number = random.random()
print(number)

guess = random.randint(1, user_input)
print(guess)

count = 0
counter = 0
while count < 5:
    number = int(input())
    print(random.randint(1, 21))
    count += 1
    counter += number
    print(counter)
