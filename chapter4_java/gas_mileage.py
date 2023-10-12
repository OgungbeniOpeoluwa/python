counter = int(input("press 1 to start or press -1 to quit"))
gallon_count = 0
miles_count = 0
while counter != -1:
    gallon = float(input("Enter the gallons used :"))
    gallon_count += gallon
    print(gallon_count)
    miles = float(input("Enter the miles used : "))
    miles_count += miles
    print(miles_count)
    miles_gallon = miles / gallon
    print("miles per gallon = ", miles_gallon)
    counter = int(input("press 1 to start or press -1 to quit"))

combined_miles_gallon = "{:.6f}".format(miles_count / gallon_count)
print(f"The combined miles per gallon obtained from the tankful is {combined_miles_gallon}")

# .format is an old way of formating a string in python, from python 3.6 f string was introduced, string is cleaner and easier
# you can leave this, so u know how to use .format method as well.
