lists = []
for number in range(10):
    user_input = int(input("Enter a number: "))
    lists.append(user_input)

result = sorted(lists)
print(f'the two largest number is {result[8]} and {result[9]}')
