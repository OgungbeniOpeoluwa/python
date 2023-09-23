def multiples_of_five_and_3(stop_number: int):
    starter = 1
    while starter != stop_number:
        if starter / 3 == 5 and starter / 5 == 3:
            print("FizzBuzz")
        elif starter % 3 == 0:
            print("Fizz")
        elif starter % 5 == 0:
            print("buzz")
        else:
            print(starter)
        starter += 1


multiples_of_five_and_3(50)
