number = int(input("Enter your age: "))
age_1 = number < 18
age2 = number > 18

total = 1
total2 = 2

match number:
    case 1:
        print("you are not eligible")

    case 2:
        print("you are eligible")