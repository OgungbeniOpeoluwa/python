def main_menu():
    user_input = int(input("""press:
              1. phoneBook
              2. messages
              3. chat
              4. callRegister
              5. tones
              6. settings
              7. call divert
              8. games
              9. calculator
              10. remainder
              11. clock
              12. profiles
              13. simServices
              14. exit
              """))
    if user_input == 1:
        return phonebook()


# case 2:
#     print("message")
#     nokia_function.messages()
# case 3:
#     print("Chat")
#     nokia_function.chat()
# case 4:
#     print("Call Register")
#     nokia_function.callRegister()
# case 5:
#     print("Tones")
#     nokia_function.tones()
# case 6:
#     print("Setting")
#     nokia_function.settings()
# case 7:
#     print("Call Divert")
#     nokia_function.callDivert()
# case 8:
#     print("Games")
#     nokia_function.games()
# case 9:
#     print("Calculator")
#     nokia_function.calculator()
# case 10:
#     print("Reminders")
#     nokia_function.reminders()
# case 11:
#     print("Clock")
#     nokia_function.clock()
# case 12:
#     print("Profiles")
#     nokia_function.profiles()
# case 13:
#     print("SIM Services")
#     nokia_function.simServices()


def phonebook():
    print("""
                press
                1. Search
                2. ServiceNos
                3. AddName
                4. Erase
                5. Edit
                6. Assign Tone
                7. Send b'Card
                8. Options
                9. Speed
                10. Voice Tags
                11.Main Menu
                """)
    inputsr = int(input("Enter response: "))
    if inputsr == 1:
        return "search"
    elif inputsr == 2:
        return "service nos"
    elif inputsr == 3:
        return "add name"
    elif inputsr == 4:
        return "edit"
    elif inputsr == 5:
        return "Edit"
    elif inputsr == 6:
        return "Assign Tone"
    elif inputsr == 7:
        return "send b' card"
    elif inputsr == 8:
        print("""
                    if you like to continue,
                    press
                    1. Type Of View
                    2. Memory Status
                    3. Go Back
                    4.Main Menu
                    """)
        number = input()
        if number == 1:
            return "type Of View on mode"
        elif number == 2:
            return "memory Status on mode"
        elif number == 3:
            return phonebook()
        else:
            main_menu()
    elif inputsr == 9:
        return "Speed dial"
    elif inputsr == 10:
        return "voice tags"
    else:
        return main_menu()


def messages():
    message = input("""
    1. write messages
    2. inbox
    3. outbox
    4. picture messages
    5.Templates
    6.smileys
    7.message settings
    8.info service 
    9. voice mail
    10.service command editor
    11. Main Menu
    """)
    if message == 1:
        return "Write message"
    elif message == 2:
        return "Inbox"
    elif message == 3:
        return "OutBox"
    elif message == 4:
        return "Picture Messages"

    elif message == 5:
        return "Templates"
    elif message == 6:
        return "Smiley"
    elif message == 7:
        settings = input("""
            1. Set1
            2. common
            3.Go back
            4.main menu""")
        if settings == 1:
            setting = input("""
                         1. Message center Number
                         2.Message sent as
                         3.Message validity
                         4. Go back
                         5.main menu""")
            if setting == 1:
                return "Message Center Number"
            elif setting == 2:
                return "Message Sent as"
            elif setting == 3:
                return "Message Validity"
            elif setting == 4:
                return messages()
            else:
                return main_menu()
        elif settings == 2:
            common = input("""
                          1.Delivery Report
                          2.Reply Via Same Center
                           3.Character support
                           4.go back
                           5.main menu""")
            if common == 1:
                return "Delivery Report"
            elif common == 2:
                return "Reply Via Same Center"
            elif common == 3:
                return "Character support"
            elif common == 4:
                return messages()
            else:
                return main_menu()
        elif settings == 3:
            return messages()
        else:
            return main_menu()
    elif message == 8:
        return "Info Services"
    elif message == 9:
        return "Voice MailBox Number"
    elif message == 10:
        return "Service Command Editor"
    else:
        return main_menu()


def chat():
    chats = input("""
                    1. Chat
                    2. Main Menu""")
    if chats == 1:
        return "Chat"
    elif chats == 2:
        return main_menu()


def callRegister():
    call = input("""
                    press
                    1. Missed call
                    2. Recieve call
                    3. Dialled Numbers
                    4. Erase recent call list
                    5. Show Call Duration
                    6. Show call Costs
                    7. Call Cost Setting
                    8. Prepaid Credit
                    9.Main Menu
                    """)
    if call == 1:
        return "Missed Call"
    elif call == 2:
        return "Recieve Call"
    elif call == 3:
        return "Dialled Numbers"
    elif call == 4:
        return "Erase Recent Call List"
    elif call == 5:
        duration = input("""
           1. Last Call Duration
           2. All Call's Duration
           3. Receive Call's Duration 
           4. Dialled Call Duration
           5. Clear Timers
           6. Go Back
            7. Main Menu""")
        if duration == 1:
            return "Last Call Duration"
        elif duration == 2:
            return "All Call's Duration"
        elif duration == 3:
            return "Receive Call Duration"
        elif duration == 4:
            return "Dialled Call Duration"
        elif duration == 5:
            return "Clear Timers"
        elif duration == 6:
            return callRegister()
        else:
            return main_menu()
    elif call == 6:
        call_cost = input("""
            1. Last Call Cost
            2.All Call Cost
            3.Clear Counters
            4.Go Back
            5. MAin Menu""")
        if call_cost == 1:
            return "Last Call Cost"
        elif call_cost == 2:
            return "All Call Cost"
        elif call_cost == 3:
            return "Clear Counters"
        elif call_cost == 4:
            return callRegister()
        else:
            return main_menu()
    elif call == 7:
        show_call = input("""
           1. Call Cost Limit
           2. Show Cost In
           3. Go Back
           4. Main Menu""")
        if show_call == 1:
            return "Call Cost Limit"
        elif show_call == 2:
            return "Show Cost In"
        elif show_call == 3:
            return callRegister()
        else:
            return main_menu()
    elif call == 8:
        return "Prepaid Credit"
    else:
        return main_menu()


def tones():
    print("""
                press
                1. Ringing Tone
                2. Ringing Volume
                3. Incoming Call Alert
                4. Composer
                5. Message Alert Tone
                6. Keypad Tones
                7. Warning and Game Tones
                8. Vibrating Alert
                9. Screen Saver
                10. Main Menu
                """);
    tone = int(input("Enter response: "))
    if tone == 1:
        return "Ringing Tones"
    elif tone == 2:
        return "Ringing Volume"
    elif tone == 3:
        return "Incoming Call Alert"
    elif tone == 4:
        return "Composer"
    elif tone == 5:
        return "Message Alert Tone"
    elif tone == 6:
        return "Keypad Tones"
    elif tone == 7:
        return " Warning and Game Tones"
    elif tone == 8:
        return "Vibrating Alert"
    elif tone == 9:
        return "Screen Saver"
    else:
        return main_menu()

def settings():
        print("""
                1. Call Setting
                2. Phone Setting
                3. Security Setting
                4. Restore Factory Settings
                5. Main Menu
                """);
        setting = int(input("Enter your response: "))
        if setting == 1:
            print("""
            1. Automatic Redial
            2. Speed Dialing
            3. Call Waiting Option
            4. Own Number Sending
            5. Phone line in use
             6. Automatic Answer
             7. Go Back
             8. Main Menu""");
            user = int(input("Enter your response: "))
            if user == 1:
                return "Automatic Redial"
            elif user == 2:
                return "Speed Dialing"
            elif user == 3:
                return "Call Waiting Option"
            elif user == 4:
                return "Own Number Sending"
            elif user == 5:
                return "Phone line in use"
            elif user == 6:
                return "Automatic Answer"
            elif user == 7:
                return settings()
            else:
                return main_menu()
        elif setting == 2:
            print("""
            1.Language
            2. Cell Waiting Options
            3. Welcome Note
            4. Network Selection
            5. Lights
            6. Confirm Sim Service Action
            7. Go Back
            8. Main Menu""");
            phone_settings = int(input("Enter your response: "))
            if phone_settings == 1:
                return "Language"
            elif phone_settings == 2:
                return " Cell Waiting Options"
            elif phone_settings == 3:
                return " Welcome Note"
            elif phone_settings == 4:
                return "Network Selection"
            elif phone_settings == 5:
                return "Lights"
            elif phone_settings == 6:
                return "Confirm Sim Service Action"
            elif phone_settings == 7:
                return settings()
            else:
                return main_menu()
        elif setting == 3:
            print("""
             1. Pin Code Request
             2. Call Barring Service
             3. Fixed Dialling
             4. Closed User Group
             5. Phone Security 
             6. Change Access Code
             7. Go back
             8. Main Menu""")
            security_setting = int(input("enter response: "))
            if security_setting == 1:
                return "Pin Code Request"
            elif security_setting == 2:
                return "Call Barring Service"
            elif security_setting == 3:
                return "Fixed Dialling"
            elif security_setting == 4:
                return "Closed User Group"
            elif security_setting == 5:
                return " Phone Security"
            elif security_setting == 6:
                return "Change Access Code"
            elif security_setting == 7:
                return settings()
            else:
                return main_menu()
        elif setting == 4:
            return "Restore Factory"
        else:
            return main_menu()


