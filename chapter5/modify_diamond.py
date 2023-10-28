from chapter5 import diamond_printing

inputs = int(input("Enter a any odd number within 1 to 19: "))
if inputs % 2 == 1:
    diamond_printing.diamond(inputs)
