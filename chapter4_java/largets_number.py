count = []
name = []
for number in range(10):
    user_input_name = input("enter your name : ")
    user_input = int(input("Enter a number of unit sold by each person: "))
    name.append(user_input_name)
    count.append(user_input)

result = max(count)
names = count.index(result)
print(f'the winner is {name[names]}:, {result}')
