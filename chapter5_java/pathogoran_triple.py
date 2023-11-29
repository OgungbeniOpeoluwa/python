def square(number):
    product = 1
    for count in range(1, 3):
        product *= number
    return product


def find_square(number):
    result = 0
    for number2 in range(1, number):
        if number2 * number2 == number:
            result = number2
    return result


result = 0
product = 0
result2 = 0
number = 0
counts = 0
total = 0
for number in range(1, 101):
    result = square(number)
    for counts in range(1, 101):
        product = square(counts)
        result2 = result + product
        total = find_square(result2)
        if total == 0:
            continue
        if result2 / total == total:
            print(f'{number:4} {counts: 4} {total: 4}')
