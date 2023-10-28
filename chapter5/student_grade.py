countA = 0
countB = 0
countC = 0
countD = 0
for number in range(1, 6):
    name = input("Enter your name: ")
    letter = input("Enter your letter grade: ")
    score = int(input("Enter your score grade: "))
    results = score // 10
    if results == 10 or results == 9:
        countA += 1
    elif results == 8:
        countB += 1
    elif results == 7:
        countC += 1
    elif results == 6:
        countD += 1
    else:
        print("you failed")
print(countA, " number of student got A")
print(countB, " number of student got B")
print(countC, " number of student got C")
print(countD, " number of student got D")
