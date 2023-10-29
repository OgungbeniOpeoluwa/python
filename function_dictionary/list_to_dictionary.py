def function_list_to_dictionary(result: list):
    dictionary = {}
    for count in result:
        if count[0] in dictionary.keys():
            result = str(count[0]).upper()
            dictionary[result] = count
        else:
            dictionary[count[0]] = count
    return dictionary


def difference_in_list(result):
    product = max(result) - min(result)
    return product


def two_list_to_dictionary(result1: list, result2: list):
    result = {}
    for count in range(len(result1)):
        result[result1[count]] = result2[count]

    return result


def remove_duplicate_numbers_function(result: list, number):
    counter = 0
    count = 0
    results = []
    while counter < len(result):
        for counts in range(len(result)):
            if result[counter] == result[counts]:
                count += 1
        if count > number:
            results.append(result[counter])
        counter += count
        count = 0
    return results


def remove_multiple_string_function(result):
    product = []
    counter = ""
    for count in result:
        if count.isalpha():
            product.append(count)
        else:
            for counts in count:
                if counts.isalpha():
                    counter += counts
                else:
                    if counter.isalpha():
                        product.append(counter)
                    counter = ""
    return product


def split_list_function(result: list):
    results = []
    returns = []
    product = len(result) // 2
    for count in range(product):
        results.append(result[count])
    for counts in range(product, len(result)):
        returns.append(result[counts])
    return results, returns
