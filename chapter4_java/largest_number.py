count = 0
largest = 0
user_input_name = ""
while count != 10:
    user_input_name = input("enter your name : ")
    user_input = int(input("Enter number of unit sold: "))
    if user_input > largest:
        largest = user_input

    count += 1
print(user_input_name, "has the highest unit which is: ", largest)

