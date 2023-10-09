import card_validation

number = input("Hello, Kindly Enter Card Details To Verify: ")
result = len(number)
while result < 13 or result > 16:
    number = input("Hello, Kindly Enter Card Details To Verify: ")
    result = len(number)
card_validation.display_result(number)
stop = int(input("Will like to validate another card if yes; press(0)else (-1)"))
while stop != -1:
    number = input("Hello, Kindly Enter Card Details To Verify: ")
    result = len(number)
    while result < 13 or result > 16:
        number = input("Hello, Kindly Enter Card Details To Verify: ")
        result = len(number)
    card_validation.display_result(number)
    stop = int(input("Will like to validate another card if yes; press(0)else (-1)"))



