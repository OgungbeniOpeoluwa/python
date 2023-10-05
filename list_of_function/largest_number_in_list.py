number = [15, 20, 25, 20, 10, 5]
maximum = number[0]
for numb in range(1, len(number)):
    if number[numb] > maximum:
        maximum = number[numb]

print("the maximum number is ", maximum)
