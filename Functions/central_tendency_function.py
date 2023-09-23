from Functions.arrangement_function import sorting_numbers


def median(numbers: list):
    total = sorting_numbers(numbers)
    value = len(total)
    if value % 2 == 0:
        result1 = total[value // 2]
        result2 = total[value // 2 - 1]
        result = (result1 + result2) // 2
        return result
    else:
        result1 = total[value // 2]
        return result1


def mean(numbers: list):
    total = 0
    for numb in numbers:
        total += numb
    average = total / len(numbers)
    return average


user_input = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]
print(median(user_input))
print(mean(user_input))
