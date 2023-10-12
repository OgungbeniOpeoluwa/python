def tax_calculator_function(earnings):
    result = 0
    if earnings <= 30000:
        result = 0.15 * earnings
    if earnings > 30000:
        result = 0.2 * earnings
    return result


count = 0
while count <= 3:
    name = input("Enter your name: ")
    earnings = int(input("Enter earnings for the year :"))
    result = tax_calculator_function(earnings)
    print(f'{name} your total tax is {result}')
