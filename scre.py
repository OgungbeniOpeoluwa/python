num = 1
total = 0
while num < 10:
    number = int(input("Enter your score : "))
    total += number
    num += 1

average = total / num
print(f' the average of the score is {average}')

