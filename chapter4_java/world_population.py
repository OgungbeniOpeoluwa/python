population = 8045311447
growth_rate = 0.088
total = 0
diffrences = 0
print("Year  Population  Numeric Increase")
for n in range(1, 76):
    total = population * (1 + (growth_rate ** n))
    diffrences = total - population
    print(f'{n}  {total: >3}  {diffrences: > 3}')
