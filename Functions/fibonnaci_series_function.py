def fibonacci_series(stop_number: int):
    first_number = 0
    second_number = 1
    for numbers in range(1, stop_number):
        if first_number <= 50:
            print(first_number, end=" ")
        result = first_number + second_number
        first_number = second_number
        second_number = result


fibonacci_series(50)
