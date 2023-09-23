def square_cube(stop_number: int):
    print(f'number  square  cube')
    for number in range(1, stop_number):
        print(f'{number}\t{number ** 2}\t\t{number ** 3}')


square_cube(10)
