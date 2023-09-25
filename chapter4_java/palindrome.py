def palindrome(user_input: int):
    value = str(user_input)
    number = value[::-1]
    if value == number:
        return f'{number} is a palindrome number'
    else:
        return f'{number} is not a palindrome number'


print(palindrome(12111))
