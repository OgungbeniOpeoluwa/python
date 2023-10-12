user_input = input("enter a number: ")
length = len(user_input)
while length > 5:
    print("Kindly enter a valid number: ")
    user_input = input("enter a number: ")
    length = len(user_input)

number = user_input[::-1]
if user_input == number:
    print("it is a palindrome")
else:
    print("Not a palindrome")
