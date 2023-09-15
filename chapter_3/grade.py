passes = 0
failed = 0
for student in range(10):
    user_input = int(input("Enter result between 1 and 2 where 1 = pass and fail = 2:  "))
    if user_input == 1:
        passes += 1
    else:
        failed += 1
    while user_input != 1 and user_input != 2:
        user_input = int(input("kindly enter a valid number: "))
print(f' total number of student that pass is : {passes}\n total number of student that failed: {failed}')

