def palindromes(numbers: int) -> bool:
    value = str(numbers)
    result = value[::-1]
    return value == result


print(palindromes(1112131))
