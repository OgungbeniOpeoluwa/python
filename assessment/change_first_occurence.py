from assignment.geographical_zone import Geographical_zone


def change_first_occurrence_function(result: str, letter, replaces):
    results = result.count(letter)
    number = result.index(letter)
    first_word = result[0: number+1]
    for count in result:
        if results > 1:
            if letter == count:
                result = result.replace(count, replaces)
    return first_word + result[number + 1:]


