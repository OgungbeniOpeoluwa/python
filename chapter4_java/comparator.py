first_input = int(input("Enter first integer : "))
second_input = int(input("Enter second integer : "))
print(f"""  if your first number is equal to second number result is = 0, 
    if first number is greater than second number result is = 1
    if second number is greater result = -1""")

if first_input == second_input:
    print("0")
elif first_input > second_input:
    print("1")
else:
    print("-1")