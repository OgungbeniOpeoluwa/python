
def check_number(number, numb):
    numbs = len(number)
    answer = False
    for n in number:
        if n == numb:
            answer = True
    return answer


print(check_number([1, 2, 5, 6], 2))
