def palindrome(user_input):
    temp = user_input
    reverse = 0
    while user_input != 0:
        first_number = user_input % 10
        reverse = reverse * 10 + first_number
        user_input //= 10
    if temp == reverse:
        return True
    else:
        return False


print(palindrome(10000000000000000000000000000001))
