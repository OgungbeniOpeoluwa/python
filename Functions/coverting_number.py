def decimal_to_binary(number):
    answer = ""
    while number != 0:
        result = number % 2
        answer = str(result) + answer
        number //= 2
    return answer


def binary_to_decimal(number):
    product = 0
    final = 2
    result = str(number)
    numb = int(result[0]) * final
    for index, value in enumerate(result):
        if index == 0:
            continue
        numb += int(value)
        numb *= final
    return numb // 2



