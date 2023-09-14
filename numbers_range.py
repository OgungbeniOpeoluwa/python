number = int(input("Enter a number or press -1 to quit:"))
minimum = number
maximum = number

while number != -1:
    if number <= minimum:
        minimum = number

    if number >= maximum:
        maximum = number

    number = int(input("Enter a number or press -1 to quit:"))

print("The Smallest number is : ", minimum)
print("The largest number is : ", maximum)
