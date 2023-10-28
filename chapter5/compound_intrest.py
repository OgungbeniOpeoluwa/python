principal = 1000.0
rate = 0
print(f'%s    %14s     %20s     %20s     %14s   %22s   %22s  %n, Year, 5% ,6% , 7%, 8%, 9%, 10%')
for year in range(1, 11):
    for number in range(5, 11):
        rate = number / 100
        amount = principal * ((1.0 + rate) ** year)
        print(f'{year:8.2f} {amount:8.2f}', end=" ")

    print(" ")
