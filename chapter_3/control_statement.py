number = int(input("Enter a number: "))
smallest = number
largest = number

for number in range(1, 10):
    user_input = int(input("Enter a number: "))
    if user_input < smallest:
        smallest = user_input
    if user_input > largest:
        largest = user_input

print(smallest)
print(largest)
 