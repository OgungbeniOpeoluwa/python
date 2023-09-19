number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = 0
odd = 0
for count in number:
    if count % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"""number of even number : {even}
number of odd number: {odd}
""")
