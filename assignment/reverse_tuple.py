def reverse_tuple1(number: tuple):
    lists = list(number)
    result = len(number) - 1
    lists[result] = number[0]
    count = 0
    for numb in range(result, 0, -1):
        lists[count] = number[numb]
        count += 1

    return tuple(lists)


def nested_tuple(number: tuple, numbers: int, numb: int):
    result = 0,
    result2 = 2,
    total = 0,
    for count in number:
        for counter in count:
            if counter == numbers:
                result = counter
            if counter == numb:
                result2 = counter
    turple2 = (result, result2)
    return tuple(enumerate(turple2))


def unpacked_swapped_function(numbers):
    total = len(numbers) - 1
    first_index = 0
    firstnumber, secondnumber = numbers[first_index], numbers[total]
    firstnumber, secondnumber = (secondnumber, firstnumber)
    return firstnumber, secondnumber


def sorting_by_second_item(number):
    # sought = 0,
    result2 = ()
    result = len(number)
    for count in range(result):
        for counts in range(count + 2, result):
            result2 += number[counts]
            result2 += number[count]
        # result2 += number[count]
    print(result2)


print(sorting_by_second_item((('a', 23), ('b', 37), ('c', 11), ('d', 29))))

# def number_appeared_more_than_once(number: tuple):
#     result2 = (0,)
#     result = len(number)
#     result -= 1
#     for count in range(result, +2):
#         result2 += number[count]
#         result -= result
#     print(result2)


# number_appeared_more_than_once((20, 10, 15, 20, 5, 30, 10, 35, 10, 40, 45, 5))
