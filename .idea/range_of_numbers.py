number = int(input("Enter a number or pres 0 to quit: "))
maximum = 0
minimum = 0
while number != 0:
    if number < number:
        minimum = minimum + number

    if number > number :
        maximum = maximum + number

    if number == 0:
        break

    number = int(input("Enter a number or press 0 to quit"))

print(maximum)
print(minimum)

