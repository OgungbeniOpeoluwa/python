def set_card_digit(number: str):
    result = len(number)
    result2 = 0
    if 13 <= int(result) <= 16:
        result2 = number

    return result2


def length_of_card(number):
    result = len(number)
    return result


def check_first_number_validity(number):
    result = "Invalid card"
    for numbers in range(len(number)):
        if number[0] == "4":
            result = "Visa Card"
            break
        elif number[0] == "5":
            result = "Master Card"
            break
        elif number[0] == "3" and number[1] == "7":
            result = 'American Express Card'
            break
        elif number[0] == "6":
            result = "Discover Card"
            break
    return result


def validity_of_number(number):
    answer = "Invalid"
    result = doubling_second_digit(number) + oddly_place_number(number)
    if result % 10 == 0:
        answer = "Valid"
    return answer


def doubling_second_digit(number):
    temp = number[len(number)::-1]
    result = 0
    total = 0
    for count in range(1, len(temp), 2):
        result = (int(temp[count])) * 2
        if result >= 10:
            total += addition(result)
        else:
            total += result

    return total


def display_result(number):
    print(f"""
    ********************************************************
    ** Credit Card Type: {check_first_number_validity(number)}
    ** Credit Card Number : {set_card_digit(number)}
    ** Credit Card Digit Length : {length_of_card(number)}
    ** Credit Card Validity Status : {validity_of_number(number)}
    *************************************************************
         """)


def oddly_place_number(number):
    temp = number[len(number)::-1]
    result = 0
    for count in range(0, len(temp), 2):
        result += (int(temp[count]))
    return result


def addition(number):
    result = 0
    while number != 0:
        count = number % 10
        result += count
        number //= 10
    return result
