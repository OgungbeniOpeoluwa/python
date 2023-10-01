def square_root(user_input):
    for number in range(1, user_input):
        if number * number == user_input:
            return number


def square_root2(number):
    total = number
    count = 0
    for numb in range(1, number, 2):
        number -= numb
        count += 1
        if number == 0 and total // 5:
            return count
