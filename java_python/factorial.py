number = int(input("Enter a number :"))
total = 1

while 1 <= number:
    total *= number
    number -= 1

print(total)