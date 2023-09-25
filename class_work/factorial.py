total = 1
for number in range(5, 0, -1):
    total *= number
    if number == 1:
        print(number, "=", total)
        break
    print(number, "* ", end="")
