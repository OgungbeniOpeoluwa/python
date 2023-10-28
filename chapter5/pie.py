constant = 4
count = 0
result = 0
for number in range(1, 2000000, 2):
    if count % 2 == 1:
        result -= constant // number
    elif count % 2 == 0:
        result += constant // number
        count += 1
print(f'{result:.5f}')
