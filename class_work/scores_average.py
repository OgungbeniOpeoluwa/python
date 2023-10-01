def scores(*numbers):
    result = 0
    average = 0
    count = 0
    for i in numbers:
        result += i
        count += 1
    average = result / count
    return average


# plus = []
# for numb in range(10):
#     inputs = int(input("Enter your score: "))
#     plus.append(inputs)

print(scores(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
