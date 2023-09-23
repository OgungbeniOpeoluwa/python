pie = 0
count = 1
number = 1
constant = 4
while pie != 3.14159:
    if count % 2 == 1:
        pie += constant / number
    else:
        pie += (-(constant / number))
    print(f'{number} {pie:.5f}')
    number = number + 2
    count = count + 1
