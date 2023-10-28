user_input = input("Enter a letter: ")
vowel = ['a', 'e', 'i', 'o,''u']
for n in range(len(vowel)):
    if vowel[n] == user_input[n]:
        print(True)
        break
    else:
        print(False)
        break

