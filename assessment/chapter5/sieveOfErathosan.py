number = []
for count in range(1000):
    number.append(True)

for counts in range(2, 1000):
    for count in range((counts + 1), 1000):
        if count % counts == 0:
            number[count] = False
result = []
for counter in range(2, len(number)):
    if number[counter]:
        result.append(counter)

print(result)
