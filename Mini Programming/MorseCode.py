
def morseEnc(letter):
    match letter:
        case " ":
            return "/"
        case "A":
            return ".- "
        case "B":
            return "-... "
        case "C":
            return "-.-. "
        case "D":
            return "-.. "
        case "E":
            return ". "
        case "F":
            return "..-. "
        case "G":
            return "--. "
        case "H":
            return ".... "
        case "I":
            return ".. "
        case "J":
            return ".--- "
        case "K":
            return "-.- "
        case "L":
            return ".-.. "
        case "M":
            return "-- "
        case "N":
            return "-. "
        case "O":
            return "--- "
        case "P":
            return ".--. "
        case "Q":
            return "--.- "
        case "R":
            return ".-. "
        case "S":
            return "... "
        case "T":
            return "	- "
        case "U":
            return "..- "
        case "V":
            return "...- "
        case "W":
            return ".-- "
        case "X":
            return "-..- "
        case "Y":
            return "-.-- "
        case "Z":
            return "--.. "
        case "1":
            return ".---- "
        case "2":
            return "..--- "
        case "3":
            return "...-- "
        case "4":
            return "....- "
        case "5":
            return "..... "
        case "6":
            return "-.... "
        case "7":
            return "--... "
        case "8":
            return "---.. "
        case "9":
            return "----. "
        case "0":
            return "----- "


print("Welcome to Morse Code Generator")
print("--------------------------------")
print("Select Your Option")
print("1. MorseEncode")
print("2. MorseDecode")
userData = input(": ")
userList = []
finalSplit = []
if userData == "1":
    userText = input("Enter the text you want to Encode: ")
    user_text_to_list = list(userText)
    for letter in user_text_to_list:
        new_list_text = morseEnc(letter.upper())
        userList.append(new_list_text)
    newText = "".join(userList)
    print(f"Your MorseEncoded Text is :\n{newText}")
else:
    userText = input("Enter the text you want to Decode: ")
    userText_to_list = userText.split('/')
    print(userText_to_list)
    for i, s in enumerate(userText_to_list):
        if " " in s:
            finalSplit.extend(s.split(" "))
            if i != len(userText_to_list)-1:
                finalSplit.append("/")
        else:
            finalSplit.append(s)
            if i != len(userText_to_list)-1:
                finalSplit.append("/")


