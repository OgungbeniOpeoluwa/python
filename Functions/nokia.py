def phone_book():
    print("""press
        1. search
        2.service
        3 add name
        4.erase
        5.edit
        6.Assign tone
        7. send b'card
        8.option(input)
        9.speed dials
        10.voice tag
        """)

    user_input = int(input("Enter someone "))
    if user_input == 1:
        print("search")
    if user_input == 2:
        print("Service")
    if user_input == 3:
        print("add name")
    if user_input == 4:
        print("erase")
    if user_input == 5:
        print("edit")
    if user_input == 6:
        print("assign tone")
    if user_input == 7:
        print("send b ' card")
    if user_input == 8:
        user_input2 = input(""""
            1. type of view
            2. Memory status
            3. back""")
        if user_input2 == 1:
            print('Type of view')
        if user_input2 == 2:
            print('Memory Status')


phone_book()
