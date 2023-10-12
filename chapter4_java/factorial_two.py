user_input = int(input("Enter a number: "))
product = 1
divide = 0
product2 = 1
sums = 1
for n in range(1, user_input + 1):
    product *= user_input
    product2 *= n
    divide = product / product2
    sums += divide

print("Constant e is = ", sums)
