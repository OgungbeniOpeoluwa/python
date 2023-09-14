import random
sum = int(input("Enter a number within 0 and 6"))
number = random.random()
print(number)

_=random.randint(1, sum)
print(_)

count = 0
counter = 0
while count < 5:
    number = int(input())
    print(random.randint(1,21))
    count +=1
    counter += number
    print(counter)