user_input = int(input("Enter a five digit integer number: "))
while user_input < 11111 or user_input > 99999:
    user_input = int(input("Kindly Enter a five digit integer number: "))

first_digit = user_input // 10000
second_digit = user_input // 1000 % 10
third_digit = user_input // 100 % 10
fourth_digit = user_input // 10 % 10
fifth_digit = user_input % 10

reverse = str(first_digit)
reverse_two = str(second_digit)
reverse_three = str(third_digit)
reverse_fourth = str(fourth_digit)
reverse_fifth = str(fifth_digit)

palindrome = reverse_fifth + reverse_fourth + reverse_three + reverse_two + reverse
if user_input == int(palindrome):
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")
