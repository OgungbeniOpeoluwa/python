# for number in range(1, 51):
# if number / 3 == 5 and number / 5 == 3:
#     print("FrizzBuzz")
# elif number % 3 == 0:
#     print("Frizz")
# elif number % 5 == 0:
#     print("buzz")
# else:
#     print(number)

number = 1
while number <= 50:
    if number / 3 == 5 and number / 5 == 3:
        print("FrizzBuzz")
    elif number % 3 == 0:
        print("Frizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
    number += 1
