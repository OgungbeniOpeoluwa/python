def function_list_to_dictionary(result: list):
    dictionary = {}
    actual = 0
    for count in result:
        dictionary[count[0]] = count
        if count[0] == dictionary.keys() and dictionary.keys() != dictionary.values():
            result = str(count[0]).upper()
            dictionary[result] = count
    return dictionary


print(function_list_to_dictionary(['apple', 'banana', 'coconut','corn']))
