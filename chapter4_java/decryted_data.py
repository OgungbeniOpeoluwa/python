def decrypted_data(user_input: int):
    first_digit = user_input // 1000
    second_digit = user_input // 100 % 10
    third_digit = user_input // 10 % 10
    fourth_digit = user_input % 10

    first_digit, second_digit, third_digit, fourth_digit = third_digit, fourth_digit, first_digit, second_digit
    constant = 7
    number_one = constant - first_digit
    number_two = constant - second_digit
    number_three = constant - third_digit
    number_four = constant - fourth_digit
    total = 0
    total_two = 0
    total_three = 0
    total_four = 0
    if number_one < 0:
        total = first_digit
        total  -= first_digit
    else:
        total = first_digit + 10
        total -= constant
    if number_two < 0:
        total_two = second_digit
        total_two-=second_digit
    else:
        total_two = second_digit + 10
        total_two -= second_digit

    if number_three < 0:
        total_three = third_digit
        total_three -= third_digit
    else:
        total_three = third_digit + 10
        total_three -= constant

    if number_four < 0:
        total_four = fourth_digit
        total_four -= fourth_digit
    else:
        total_four = fourth_digit + 10
        total_four -= constant

    return f'the decrypted {total}{total_two}{total_three}{total_four}'


print(decrypted_data(2109))
