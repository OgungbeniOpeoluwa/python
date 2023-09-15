user_input2 = int(input("Enter a number: "))
smallest = user_input2
largest = user_input2
total = smallest
product = smallest
count = 1
for number in range(3):
    user_input = int(input("Enter a number: "))
    if user_input > smallest:
        largest = user_input
    else:
        smallest = user_input
    total += user_input
    product *= user_input
    count += 1
average = total / count
print(f"""the smallest number is , {smallest}
the largest number is {largest}
the average total = {average}
the total of all number ={total}
the product = {product}
""")
