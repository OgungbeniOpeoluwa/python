def equal_string(word, number):
    result = len(number)
    result2 = len(word)
    true = 0
    answer = False
    for count in word.upper():
        for counts in number.upper():
            if count == counts:
                true += 1
    if result == result2 and result == true:
        answer = True
    return answer

