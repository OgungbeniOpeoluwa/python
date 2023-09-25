def sales_calculator(*unit_sold):
    result = 0
    count = 0
    for number in unit_sold:
        count += number
    result = 200 + 0.09 * count
    return result
