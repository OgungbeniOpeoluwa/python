def print_asterik(number):
    for counter in number:
        print(" * " * counter)


result = []
for count in range(5):
    user_input = int(input("Enter a number between 1 and 30 "))
    result.append(user_input)
print_asterik(result)
