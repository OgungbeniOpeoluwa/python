def mystery(numbers):
    y = 0
    for value in numbers:
        y += value ** 2
    return y


print(mystery([1, 2, 3, 4, 5]))
