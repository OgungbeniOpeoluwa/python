def square_root2(number):
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
    if total // 5:
        return f'{total2:.4}'


print(square_root2(169))
