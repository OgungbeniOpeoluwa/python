import personaity_result


def question():
    response1 = []
    response2 = []
    response3 = []
    response4 = []
    question1 = [["A. expend energy,enjoy groups", "B.conserves energy ,enjoy-one on - one"],
                 ["A. more outgoing,think out loud", "B.more reserved,think to yourself"],
                 ["A. seek many task , public activities,interaction with others",
                  "B. seek private, solitary ,activities with quiet to ,concentrate"],
                 ["A. external,communicative,express yourself", "B. internal,reticent,keep to yourself"],
                 ["A. active, initiate", "B. reflective, deliberate"]]
    question2 = [["A. Interpret literally", "B.look for meaning and possibilities"],
                 ["A. Practical, realistic, experimental", "B.imaginative,innovative,theoretical"],
                 ["A. standard,usual,conventional", "B. different,novel,unique"],
                 ["A. focus on here-and-now", "B. look to the future,global perspective,big picture"],
                 ["A. facts, things,what is", "B.idea,dreams,what could be,philosophical"]]
    question3 = [["A. logical,thinking,questioning", "  B.empathetic, feeling,accommodating"],
                 ["A. candid, straight-forward,frank ", " B.tactful,kind,encouraging"],
                 ["A. firm,tend to criticize,,hold the line ", "B. gentle,tend to appreciate"],
                 ["A. tough-minded,just", "   B.tender-hearted,merciful"],
                 ["A. matter of fact,issue-oriented ", " B.sensitive ,people-oriented,compassionate"]]
    question4 = [["A. organized,orderly", "B.flexible,adaptable"],
                 ["A. plan schedule", "B.unplanned,spontaneous"],
                 ["A. regulated structured", "B.easy going,live and let live"],
                 ["A. preparation,plan ahead", "B. go with the flow,adapt as you go"],
                 ["A. Control, govern", "B.latitude, freedom"]]
    for value in question1:
        for val in value:
            print(val, " ", end=" ")
        print()
        name = input().upper()
        while name != "A" and name != "B":
            print("Expected A or B as response")
            name = input().upper()
        if name == "A":
            response1.append(value[0])
        else:
            response1.append(value[1])

    for value in question2:
        for index in value:
            print(index, " ", end=" ")
        print()
        name = input().upper()
        while name != "A" and name != "B":
            print("Expected A or B as response")
            name = input().upper()
        if name == "A":
            response2.append(value[0])
        else:
            response2.append(value[1])

    for numb in question3:
        for index in numb:
            print(index, " ", end=" ")
        print()
        name = input().upper()
        while name != "A" and name != "B":
            print("Expected A or B as response")
            name = input().upper()
        if name == "A":
            response3.append(numb[0])
        else:
            response3.append(numb[1])

    for numb in question4:
        for index in numb:
            print(index, " ", end=" ")
        print()
        name = input().upper()
        while name != "A" and name != "B":
            print("Expected A or B as response")
            name = input().upper()
        if name == "A":
            response4.append(numb[0])
        else:
            response4.append(numb[1])
    print()
    result = 0
    result2 = 0
    personality = [["E", "I"], ["S", "N"], ["T", "F"], ["J", "P"]]
    count = ""
    counts = 0
    results = [response1, response2, response3, response4]
    for numb in results:
        for numbs in numb:
            print(numbs)
            if numbs.startswith("A"):
                result += 1
            else:
                result2 += 1
        print()
        print("Number of A:", result)
        print("Number of B: ", result2)
        if result > result2:
            count += personality[counts][0]
        else:
            count += personality[counts][1]
        result = 0
        result2 = 0
        counts += 1
        print()
    return personaity_result.personality_result(count)


question()
