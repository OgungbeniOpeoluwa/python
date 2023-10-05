number = [15, 20, 25, 20, 10, 5]
minimum = number[0]
for numb in range(1, len(number)):
    if number[numb] < minimum:
        minimum = number[numb]

print("the minimum number is ", minimum)
