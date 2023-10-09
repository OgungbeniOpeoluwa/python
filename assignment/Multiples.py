def multipleTriple(numbers):
    result = []
    total = 0
    for numb in numbers:
        total = numb **3
        result.append(total)
    return result


print(multipleTriple([3, 7, 2, 6, 5]))
