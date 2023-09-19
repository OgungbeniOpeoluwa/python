principal = 1000
percentage_return = 7 / 100

for year in range(1, 31):
    amount = principal * (1 + percentage_return) ** year
    print(f""" YEAR\t\t\tAMOUNT \n  {year} \t\t\t{amount}
    """)
