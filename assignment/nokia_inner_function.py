def addition(numbers):
    total = 0
    while numbers != 0:
        count = numbers % 10
        total += count
        numbers //= 10
    return total


def multiplication(numbers):
    total = 1
    while numbers != 0:
        count = numbers % 10
        total *= count
        numbers //= 10
    return total


def square_root(number):
    total = number
    count = 0
    for numb in range(1, number, 2):
        number -= numb
        if number < 0:
            continue
        count += 1
    sums = total / count + count
    division = sums / 2
    result = total / division
    total2 = (division + result) / 2
    return total2


def square(number):
    for count in range(number):
        if count * count == number:
            return count
