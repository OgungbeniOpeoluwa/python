population = 8045311447
growth_rate = 0.088
print(f'Number  Population   Numerical Increase')
for number in range(1, 76):
    total = population * ((1 + growth_rate) ** number)
    difference = total - population
    print(f'{number} \t\t{total} \t{difference}')
