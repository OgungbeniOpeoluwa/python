for number in range(1, 10):
    for numb in range(number, 10):
        print("  ", end="")
    for numb in range(1, number):
        print("  ", end="")
    for numb in range(2, number):
        print("* ", end="")
    print()

for numbers in range(1, 10):
    for numb in range(1, numbers):
        print("  ", end="")
    for numb in range(numbers, 10):
        print("  ", end="")
    for numb in range(numbers, 9):
        print("* ", end="")
    print()
