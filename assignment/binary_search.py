def binary_search(number: list, key):
    low = 0
    high = len(number) - 1
    while low <= high:
        guess = (low + high)
        result = number[guess]
        if result == key:
            return guess
        if result < key:
            return guess + 1
        if result > key:
            return guess - 1
    return None


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 7))
