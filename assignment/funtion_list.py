def largest_element(numbers):
    maximum = numbers[0]
    for numb in range(1, len(numbers)):
        if numbers[numb] > maximum:
            maximum = numbers[numb]

    return maximum


def reverse(numbers):
    result = numbers[::-1]
    return result


def element_occurs(numbers, numb):
    answer = False
    for count in range(0, len(numbers)):
        if numbers[count] == numb:
            answer = True
    return answer


def oddly_place(numbers):
    number = []
    for count in range(0, len(numbers), 2):
        number.append(numbers[count])
    return number


def even_place(number):
    numbers = []
    for count in range(1, len(number), 2):
        numbers.append(number[count])
    return numbers


def running_total(numbers):
    result = 0
    for count in range(len(numbers)):
        result += numbers[count]
    return result


def palindrome(word):
    answer = False
    result = word[::-1]
    if result == word:
        answer = True
    return answer


def cocatinating_two_list(numbers, number):
    result = []
    for count in range(len(numbers)):
        result.append(numbers[count])
    for counts in range(len(number)):
        result.append(number[counts])
    return result


def cocatinating_in_between(numbers, number):
    control = 0
    result = []
    count = len(number)
    for count in range(len(numbers)):
        result.append(numbers[count])
        result.append(number[control])
        control += 1
        count -= 1
    while count != 0:
        result.append(number[control])
        control += 1
        count -=1

    return result


def digit_to_list(*numbers):
    result = []
    total = len(numbers)
    for count in range(total):
        result.append(numbers[count])
    return result


def sums_forloop(number):
    result = 0
    for numb in range(len(number)):
        result += number[numb]
    return result


def sums_whileloop(number):
    result = 0
    count = 0
    while count < len(number):
        result += number[count]
        count += 1
    return result
