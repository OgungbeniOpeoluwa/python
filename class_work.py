user_input = int(input("Enter a number :"))
user_input1 = int(input("Enter a number :"))
user_input2 = int(input("Enter a number :"))
if user_input > user_input1 and user_input > user_input2:
    print(user_input, "is the highest")
elif user_input1 > user_input and user_input1 > user_input2:
    print(user_input1, "is the highest")
else:
    print(user_input2, "is the highest")

# Assume that if user_input is the maximum
# just want to tell you ooo

maximum = user_input

if user_input1 > maximum:
    maximum = user_input1
if user_input2 > maximum:
    maximum = user_input2
print(maximum)
