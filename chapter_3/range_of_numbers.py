numbers = [9, 11, 22, 34, 17, 22, 34, 22, 40, 34]

for numbs in range(0, len(numbers)):
    for index in range(numbs + 1, len(numbers)):
        if numbers[numbs] > numbers[index]:
            numbers[numbs], numbers[index] = numbers[index], numbers[numbs]
print(numbers)

result = len(numbers)
if result % 2 == 0:
    result1 = numbers[result // 2]
    result2 = numbers[(result // 2) - 1]
    result3 = (result1 + result2) / 2
    print("The median is : ", result3)
else:
    result1 = numbers[result // 2]
    print("The median is : ", result1)
total = 0
for lists in numbers:
    total += lists
divide = total / result
print("The mean is : ", divide)

count = 0
for n in numbers:
    if n > 1:
        count += 1
print(count)
