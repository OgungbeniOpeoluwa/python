def sum_of_two_extremes(number):
    result = max(number)
    result2 = min(number)
    return result + result2


user_input = int(input("Enter number of value you will input: "))
result = []
for count in range(user_input):
    number = int(input("Enter number: "))
    result.append(number)
print(sum_of_two_extremes(result))
