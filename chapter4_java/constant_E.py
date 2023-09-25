user_input = int(input("Enter number of term: "))
product = 1
result = 1.0
for number in range(1, user_input + 1):
    product = product * (1.0 / number)
    result += product
print(result)
