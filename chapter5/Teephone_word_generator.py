import random


def wordGeneratorFunction(number: str):
    result = ""
    dictionary = {"2": ["a", "b", "c"],
                  "3": ["d", "e", "f"],
                  "4": ["g", "h", "i"],
                  '5': ["j", "k", "l"],
                  '6': ["m", "n", "o"],
                  '7': ["p", "r", "s"],
                  '8': ["t", "u", "v"],
                  '9': ["w", "x", "y"]}
    for numb in number:
        numbs = random.randint(0, 2)
        results = dictionary.get(numb)
        returns = results[numbs]
        result += returns
    return result
