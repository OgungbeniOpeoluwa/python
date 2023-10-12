inputs = int(input("Enter a number: "))
passed = 0
fail = 0
studentCounter = 1
while studentCounter <= 10:
    result = int(input("Enter exam result(1 = pass and 2 = fail: "))
    while result != 1 and result != 2:
        print("Enter a valid number :")
        result = int(input("Enter exam result(1 = pass and 2 = fail: "))

    if result == 1:
        passed = passed + 1

    else:
        fail = fail + 1
        studentCounter += 1

    print("number of passes : ", passed)
    print("number of people who failed : ", fail);
    if passed > 8:
        print("Bonus to instructor")
