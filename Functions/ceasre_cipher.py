def arranged_alphabet(key):
    letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
              "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    arranged_letter = []
    result = len(letter) - key
    for counts in range(key):
        arranged_letter.append(letter[result])
        result += 1
    for count in range(result - key):
        arranged_letter.append(letter[count])
    return arranged_letter


def encrypt(letters, key):
    letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
              "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    result = arranged_alphabet(key)
    counter = ""
    for alphabet in letters:
        for counts, value in enumerate(letter):
            if alphabet == value:
                counter = counter + result[counts]
    return counter


def decrypt(letters, key):
    letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
              "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    result = arranged_alphabet(key)
    counter = ""
    for alphabet in letters:
        for counts, value in enumerate(result):
            if alphabet == value:
                counter = counter + letter[counts]
    return counter
