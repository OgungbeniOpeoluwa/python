def factorial_function(numbers):
    total = 1
    while numbers > 0:
        for number in range(numbers, 1, -1):
            total *= number
        return total


user_input = int(input("Enter a number: "))
print(factorial_function(user_input))
