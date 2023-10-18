number = [[25, 50, 75], [40, 50, 60], [75, 65, 80]]
numbers = []
total = 0
for ide in number:
    for n in ide:
        total = n + total
    average = total / len(number)
    print(total, average)
    total = 0
