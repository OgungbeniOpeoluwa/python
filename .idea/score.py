score = int(input("enter your score: "))
counter = 0;
total = 0
while score != 0:
    total += score
    counter += 1
    score = int(input("enter your score: "))

average = total / counter
print(f' the average score is {average:.2f}')