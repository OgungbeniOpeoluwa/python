def global_warming_question():
    answer = ["c", 'a', 'c', 'c', 'b']
    result = 0
    results = ""
    for count in range(1, 6):
        if count == 1:
            print("""
                  1. What is the primary greenhouse gas responsible for global warming
                  a. Oxygen
                  b.Nitrogen
                  c. carbon dioxide(Co2);
                  d. Hydrogen""")
            inputs = input("Please choose the correct answer by indicating the letters: ")
            if inputs == answer[0]:
                result += 1

        elif count == 2:
            print("""
                            2. Which is a consequence of global warming ?
                            a. Rising sea level
                            b. Decreased frequency of Hurricanes
                            c. Reduced temperature Worldwide
                            d. Increased Snowfall in polar regions
                            """)
            inputs = input("Please choose the correct answer by indicating the letters: ")
            if inputs == answer[1]:
                result += 1
        elif count == 3:
            print("""
                            3. What is the Primary Cause of Global Warming?
                            a.Natural climate Variability
                            b. Solar Activity
                            c. Human activities, such has burning fossil fuels
                            d. Volcanic eruptions """)
            inputs = input("Please choose the correct answer by indicating the letters: ")
            if inputs == answer[2]:
                result += 1

        elif count == 4:
            print("""
                            4.What is one way individuals can reduce their carbon footprint and
                              help combat global warming ? 
                            a. using plastics product
                            b. increasing energy consumption
                            c. reducing, reusing and recycling
                            d.  Driving alone in gas-guzzzling cars""");
            inputs = input("Please choose the correct answer by indicating the letters: ")
            if inputs == answer[3]:
                result += 1
        else:
            print("""
                            5. What are some potential consequences of global warming, as highlighted by climate change advocates?
                            a) Increased crop yields and agricultural productivity
                            b) Rising sea levels and coastal flooding
                            c) More stable weather patterns and fewer extreme events
                            d) Decreased global temperatures""");
            inputs = input("Please choose the correct answer by indicating the letters: ")
            if inputs == answer[4]:
                result += 1
        if result == 5:
            results = "Excellent,you score ", result
        elif result == 4:
            results = "very Good, you score ", result
        else:
            results = ("""
                    Time to brush up on your knowledge of global warming..check this website out
                                            Websites for Climate Change Advocates:
                                            1. Environmental Defense Fund
                             
                                            2. Climate Reality Project
                                            3. global warming policy foundation""")
    return results


print(global_warming_question())
stopper = int(input("Will you like to try again : if yes enter(1) else(0):"))
while stopper != 0:
    print(global_warming_question())
    stopper = int(input("Will you like to try again : if yes enter(1) else(0):"))
