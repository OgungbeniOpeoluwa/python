number = int(input("Enter a number"))
positive = 0
negative = 0
count = 1
while number != 0:
    if number > 0:
        positive += 1
    if number < 0:
        negative += 1

    if number == 0:
        count += number
    number = int(input("Enter a number"))

print("The total number of positive numbers is :", positive)
print("The total number of negative numbers is :", negative)
print("The total number of count numbers is :", count)




