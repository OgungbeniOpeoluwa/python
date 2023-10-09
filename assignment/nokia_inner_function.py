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


def subtraction(number):
    result = len(number)
    total = 1
    for count in range(result):
        total *= 10
    first_digit = number // total
    total = first_digit
    product = total // 10
    while total != 0:
        count = number // product % 10
        total -= count
        total //= 10
    return total


print(subtraction(544))
