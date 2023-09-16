number = int(input("Enter a number : "))
number1 = int(input('Enter a number :  '))

total = number + number1

print(total)

while number != 0:
    number2 = int(input('Enter a number 1 to continue or pres 0 to quit : '))
    if number2 == 0:
        break
    if number2 == 1:
        number = int(input("Enter a number : "))
        number1 = int(input('Enter a number : '))
        total = number + number1
        print(total)
