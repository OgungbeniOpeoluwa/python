def diamond(number):
    for count in range(number):
        for counts in range(count, 10):
            print("  ", end=" ")
        for counts in range(0, count):
            print("* ", end=" ")
        for counts in range(1, count):
            print("* ", end=" ")
        print("  ")
    for count in range(0, number+1):
        for counts in range(0, count):
            print("  ", end=" ")
        for counts in range(count, number+1):
            print("* ", end=" ")
        for counts in range(count, number):
            print("* ", end=" ")
        print("  ")
