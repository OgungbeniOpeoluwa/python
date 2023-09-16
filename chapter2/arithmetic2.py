number = int(input("Enter a number : "))
number1 = int(input("Enter second number :"))
number2 = int(input("Enter third number"))

sum = number + number1 + number2
product = number * number1 * number2
average = sum / 3
smallest = min(number, number1, number2)
largest = max(number, number1, number2)

print(sum)
print(product)
print(smallest)
print(average)
print(largest)
