from collections import Counter


def return_string_in_dictionary(result: str):
    # number = {}
    # for count in result:
    #     results = result.count(count)
    #     number[count] = results
    # return number
    return {k: result.count(k) for k in result}


print(return_string_in_dictionary('google.com'))



