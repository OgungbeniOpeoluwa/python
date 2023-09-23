def sorting_numbers(numbers: list):
    for numb in range(0, len(numbers)):
        for numbs in range(numb + 1, len(numbers)):
            if numbers[numb] > numbers[numbs]:
                numbers[numb], numbers[numbs] = numbers[numbs], numbers[numb]

    return numbers


print(sorting_numbers([10, 20, 15, 25, 5, 30, 35, 20, 10, 20]))
