scores = []
score = int(input("Enter your score"))
scores.append(score)
result = scores[0]
minimum = scores[0]
maximum = scores[0]
odd = []
if score % 2 == 1:
    odd.append(score)

for number in range(1, 10):
    score = int(input("Enter your score : "))
    result += score
    scores.append(score)
    if scores[number] > maximum:
        maximum = scores[number]
    if scores[number] < minimum:
        minimum = scores[number]
    if scores[number] % 2 == 1:
        odd.append(scores[number])
average = result / 10

print("the average is : " , average)
print(scores)
print("the sum : ", result)
print("the maximum number is: ", maximum)
print("the minimum is : ", minimum)
print("the odd number is : ", odd)
