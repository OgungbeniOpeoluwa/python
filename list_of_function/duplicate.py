numbers = [15, 20, 25, 20, 10, 5]
numb = list(set(numbers))

print(numb)

numbs = []
for number in range(len(numbers)):
    for count in range(number +1,len(numbers)):
        if numbers[number] == numbers[count]:
            numbers[count] = 0
for numb in numbers:
    if numb != 0:
        numbs.append(numb)


print(numbs)
print(numbers)