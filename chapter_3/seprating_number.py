user_input = int(input("Enter a five Digit Number: "))
tempVariable = user_input
number = 10000
sums = 0
while number != 0:
    total = user_input // number % 10
    sums = sums * 10 + total
    number //= 10
print(sums)
