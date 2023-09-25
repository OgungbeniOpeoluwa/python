def encrypted_data(user_input: int):
    first_digit = user_input // 1000
    second_digit = user_input // 100 % 10
    third_digit = user_input // 10 % 10
    fourth_digit = user_input % 10

    first_sum = (first_digit + 7) % 10
    second_sum = (second_digit + 7) % 10
    third_sum = (third_digit + 7) % 10
    fourth_sum = (fourth_digit + 7) % 10

    first_sum, second_sum, third_sum, fourth_sum = third_sum, fourth_sum, first_sum, second_sum
    return f'Encrypted data is: {first_sum}{second_sum}{third_sum}{fourth_sum}'


print(encrypted_data(3254))
