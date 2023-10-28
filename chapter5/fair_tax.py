total = 0
constant = 0.23
stoper = int(input("FAIR TAX CALCULATOR,ENTER 1 TO CONTINUE OR PRESS 0 TO STOP:"))
while stoper != 0:
            print("""
                    CHOOSE THE RANGE YOUR HOUSEHOLD FALL IN:
                    1. A person
                    2. couple 
                    3. A person and a dependent
                    4. Couple and 1 dependant 
                    5. 1 person and 2 dependents
                    6. Couple and 2 dependents 
                    7. 1 person and 3 dependents 
                    8. Couple and 3 dependents
                    9. 1 person and 4 dependents
                    10 Couple and 4 dependents 
                    11. 1 person and 5 dependents 
                    12. Couple and 5 dependents
                    13. 1 person and 6 dependents 
                    14. Couple and 6 dependents
                    15.1 person and 7 dependents 
                    16. Couple and 7 dependents""")
            user_input = int(input())
            if user_input == 1:
                    spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                    total = (spending * constant) - 247
                    print("Your monthly fair tax estimation is  : $" ,total)
            elif user_input == 2:
                    spendings = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                    total = (spendings * constant) - 494
                    print("Your monthly fair tax estimation is  : $", total)
            elif user_input == 3:
                   spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                   total = (spending * constant) - 334
                   print("Your monthly fair tax estimation is :$ " , total)
            elif user_input == 4:
                    spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                    total = (spending * constant) - 581;
                    print("Your monthly fair tax estimation is :$ " , total)
            elif user_input == 5:
                    spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                    total = (spending * constant) - 421;
                    print("Your monthly fair tax estimation is  :$ ",)
            elif user_input == 6:
                    spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                    total = (spending * constant) - 668;
                    print("Your monthly fair tax estimation is  :$ ",total)
            elif user_input == 7:
                      spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                      total = (spending * constant) - 508
                      print("Your monthly fair tax estimation is :$ ", total)
            elif user_input == 8:
                    spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                    total = (spending * constant) - 755;
                    print("Your monthly fair tax estimation is :$ ", total)

            elif user_input == 9:
                    spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                    total = (spending * constant) - 595
                    print("Your monthly fair tax estimation is : $ ", total)
            elif user_input == 10:
                    spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                    total = (spending * constant) - 842
                    print("Your monthly fair tax estimation is  :$ ",total)
            elif user_input == 11:
                    spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                    total = (spending * constant) - 682
                    print("Your monthly fair tax estimation is :$ " ,total)
            elif user_input == 12:
                    spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                    total = (spending * constant) - 929
                    print("Your monthly fair tax estimation is  :$ ",total)
            elif user_input == 13:
                    spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                    total = (spending * constant) - 769
                    print("Your monthly fair tax estimation is  :$ ", total)
            elif user_input == 14:
                    spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                    total = (spending * constant) - 1016
                    print("Your monthly fair tax estimation is  :$ ", total)
            elif user_input == 15:
                    spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                    total = (spending * constant) - 856
                    print("Your monthly fair tax estimation is  :$ ",total)
            else:
                    spending = int(input("KINDLY INPUT MONTHLY EXPENSES FOR THE MONTH:"))
                    total = (spending * constant) - 1103
                    print("Your monthly fair tax estimation is  :$ " ,total)
            stoper = int(input("FAIR TAX CALCULATOR,ENTER 1 TO CONTINUE OR PRESS 0 TO STOP:"))




