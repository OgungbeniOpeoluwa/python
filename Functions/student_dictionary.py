# student_age = {"dike": 33, "ope": 25, "melody": 20, "precious": 27}
# name = input("Enter your name :").lower()
# for names, age in student_age.items():
#     if names == name:
#         print(f'Hi {name},you are {age} years old')
#         break
# else:
#     added_age = int(input("Enter your age : "))
#     student_age[name] = added_age
#     inputs = student_age.get(name)
#     print(f' hi {name},you are {inputs} years old')


def student_dictionary(name, age=0):
    student_age = {"dike": 33, "ope": 25, "melody": 20, "precious": 27}
    returns = 0
    for k, v in student_age.items():
        if k == name:
            returns = v
            break
    else:
        student_age[name] = age
        inputs = student_age.get(name)
        returns = inputs
    return returns
