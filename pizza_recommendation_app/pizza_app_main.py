from pizza_recommendation_app import pizza_main
print("""
     WELCOME TO TIFF PIZZA PALACE
       THIS ARE THE PIZZA BOX SIZE THAT ARE  AVAILABLE
        * LARGE
        * MEDIUM
        * SMALL
        WE ALSO HAVE DIFFERENT STOMACH SLICE
        HUNGRY = 2
        SUPER_HUNGRY = 4
        CLASSIC = 1 """)
user_inputs = input("Enter preferable box size: ").lower()
while user_inputs != "big" and user_inputs != "medium" and user_inputs != "small":
    user_inputs = input("Enter preferable box size: ").lower()
hungry = int(input("Enter number of HUNGRY: "))
super_hungry = int(input("Enter number of SUPER_HUNGRY : "))
classic = int(input("Enter number of CLASSIC:"))
print(pizza_main.pizza_recommendation_app(user_inputs, hungry, super_hungry, classic))
