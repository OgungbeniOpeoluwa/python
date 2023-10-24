def function_of_prime(number):
    result = []
    for count in range(2, number):
        while number % count == 0:
            number /= count
            result.append(count)
    return result
