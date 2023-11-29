def check_number_is_divisible_by_three():
    return sum({i for i in range(31) if i % 3 == 0})


print(check_number_is_divisible_by_three())
