def display_table(first_list: list):
    count = 0
    for counts in range(len(first_list[count])):
        count += 1
        print(f'\t{counts:<3}', end="\t")

    print()

    for count in range(len(first_list)):
        print(count, end="\t")
        for counts in range(len(first_list[count])):
            print(f'{first_list[count][counts]:<5}', end="\t")
        print()


display_table([[1, 2, 3, 4, 5], [6, 7, 9, 10, 10]])

