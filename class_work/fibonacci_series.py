one = 1
zero = 0
total = zero + one

for number in range(50):
    if number < 50:
        print(number, end=" ")
    total = zero + one
    zero = one
    one = total
