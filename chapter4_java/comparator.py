def comparator_function(first_number, second_number):
    answer = -2
    if first_number == second_number:
        answer = 0
    elif first_number > second_number:
        answer = 1
    else:
        answer = -1
    return answer


first_input = int(input("Enter first integer : "))
second_input = int(input("Enter second integer : "))
print(comparator_function(first_input, second_input))
