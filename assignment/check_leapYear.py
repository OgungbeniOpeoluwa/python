def isleapYear(number):
    result = False
    if number % 4 == 0 and number % 100 != 0 and number % 400 == 0:
        result = True
    return result
