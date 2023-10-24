def salary_calculator(number_of_period):
    result = 0
    if number_of_period < 100:
        monthly_rate_per_period = 20
        result = monthly_rate_per_period * number_of_period
    else:
        division = number_of_period - 100
        monthly_rate_per_period = 20
        product = monthly_rate_per_period * (number_of_period - division)
        monthly_rate_per_period = 25
        total = monthly_rate_per_period * division
        result = product + total
    return result


name = input("Enter your name : ")
number_of_periods = int(input("Enter number of period taught in the month: "))
results = salary_calculator(number_of_periods)
print(f"""Teacher:  {name},
          periods: {number_of_periods}
          Gross salary : {results}""")
