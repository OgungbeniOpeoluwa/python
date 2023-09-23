def investment_calculator(capital_amount: int, year: int, rate: int):
    starter = 1
    value = 0
    investment_return = 0
    total = 0
    while starter <= year:
        value = rate / 100 * capital_amount
        investment_return = capital_amount + value
        capital_amount = investment_return
        print(f'your Roi is {value:.2f}, your investment is now {investment_return:.2f} , in year{starter}')
        starter += 1


investment_calculator(10000, 15, 5)
