number = int(input("Enter a number from 1 to 12 : "))
number_one = "and,a partridge in a pear tree"
number_two = "Two turtle doves"
number_three = " three French Hens"
number_four = "four Calling Birds"
number_five = " five Golden Rings"
number_six = "six Geese a Laying"
number_seven = " seven Swans are Swimming"
number_eight = "Eight maid a milking"
number_nine = "nine Ladies Dancing"
number_ten = "ten Lords a Leaping"
number_eleven = "Eleven pipers piping"
number_tweleve = "Twelve drummers drumming"
print(" ")
while number <= 12:
    match number:
        case 1:
            print("on the first day of christmas,my true love sent to me")
            print("\t",number_one)
            print(" ")
            #break

        case 2:
            print("on the second day of christmas,my true love sent to me")
            print(f'\t{number_two}\n\t{number_one}')
            print(" ")
            #break

        case 3:
            print("on the third day of christmas,my true love sent to me")
            print(f'\t{number_three}\n\t{number_two}\n\t{number_one}')
            print(" ")
            #break

        case 4:
            print("on the fourth day of christmas,my true love sent to me")
            print(f'\t{number_four}\n\t{number_three}\n\t{number_two}\n\t{number_one}')
            print(" ")
            #break

        case 5:
             print("on the fifth day of christmas,my true love sent to me")
             print(f'\t{number_five}\n\t{number_four}\n\t{number_three}\n\t{number_two}\n\t{number_one}')
             print(" ")
             #break

        case 6:
            print("on the sixth day of christmas,my true love sent to me")
            print(f'\t{number_six}\n\t{number_five}\n\t{number_four}\n\t{number_three}\n\t{number_two}\n\t{number_one}')
            print(" ")
            #break

        case 7:
            print("on the seventh day of christmas,my true love sent to me")
            print(f'\t{number_seven}\n\t{number_six}\n\t{number_five}\n\t{number_four}\n\t{number_three}\n\t{number_two}\n\t{number_one}')
            print(" ")
            #break

        case 8:
             print("on the eight day of christmas,my true love sent to me")
             print(f'\t{number_eight}\n\t{number_seven}\n\t{number_six}\n\t{number_five}\n\t{number_four}\n\t{number_three}\n\t{number_two}\n\t{number_one}')
             print(" ")
            # break

        case 9:
            print("on the ninth day of christmas,my true love sent to me")
            print(f'\t{number_nine}\n\t{number_eight}\n\t{number_seven}\n\t{number_six}\n\t{number_five}\n\t{number_four}\n\t{number_three}\n\t{number_two}\n\t{number_one}')
            print(" ")
            #break

        case 10:
            print("on the tenth day of christmas,my true love sent to me")
            print(f'\t{number_ten}\n\t{number_nine}\n\t{number_eight}\n\t{number_seven}\n\t{number_six}\n\t{number_five}\n\t{number_four}\n\t{number_three}\n\t{number_two}\n\t{number_one}')
            print(" ")

        case 11:
            print("on the eleventh day of christmas,my true love sent to me")
            print(f'\t{number_eleven}\n\t{number_ten}\n\t{number_nine}\n\t{number_eight}\n\t{number_seven}\n\t{number_six}\n\t{number_five}\n\t{number_four}\n\t{number_three}\n\t{number_two}\n\t{number_one}')
            print(" ")
            #break

        case 12:
             print("on the twelve day of christmas,my true love sent to me")
             print(f'\t{number_tweleve}\n\t{number_eleven}\n\t{number_ten}\n\t{number_nine}\n\t{number_eight}\n\t{number_seven}\n\t{number_six}\n\t{number_five}\n\t{number_four}\n\t{number_three}\n\t{number_two}\n\t{number_one}')
             print(" ")
    number += 1

