def total(numbers: list):
    results = []
    sums = 0
    for countt in numbers:
        for countss in countt:
            sums += countss
        results.append(sums)
        sums = 0
    return results


user_input = int(input("Enter number of student: "))
number_of_subject = int(input("enter number of subject : "))
result = []
for count in range(user_input):
    result.append([])
for counts in range(user_input):
    for numb in range(number_of_subject):
        score = int(input("Enter student score "))
        result[counts].append(score)
temp = total(result)
print(f'STUDENT ')
for index, students in enumerate(result):
    print(f'STUDENT {index + 1}', end=" ")
    for score in students:
        print(f' {score}', end="  ")
    print(temp[index], end=" ")
    print()
