def square_root(number):
    total = number
    count = 0
    for numb in range(1, number, 2):
        number -= numb
        count += 1
        if number == 0 and total // 5:
            return count
       # elif number != 0:


print(square_root(25))
