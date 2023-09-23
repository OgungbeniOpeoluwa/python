user_input = int(input("Enter the amount you want to investment: "))
for year in range(1, 31):
    total = 0.1 * user_input
    return_investment = user_input * (1 + 0.1)
    user_input = return_investment

    print(f'your Roi is {total:.2f}, your investment is now {return_investment:.2f} , in year{year}')
