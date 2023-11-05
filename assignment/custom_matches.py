import re


# print('true' if re.fullmatch(r'\d+[A-Z][a-z]*[A-Z][a-z]*', '1PabPa') else 'false')


def add_to_string_function(result: str):
    if result.endswith("ing"):
        result += "ly"
    else:
        number = (True if re.fullmatch(r'[a-z]{3}', result, ) else False)
        if number:
            result += "ing"
        else:
            result = result
    return result
