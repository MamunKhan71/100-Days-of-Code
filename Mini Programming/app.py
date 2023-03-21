from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='E:/Mini Programming/MorseCodeWeb/templates', static_folder='E:/Mini '
                                                                                                  'Programming'
                                                                                                  '/MorseCodeWeb/static')


def morseDec(letters):
    match letters:
        case '':
            return ''
        case "/":
            return " "
        case ".-":
            return "A"
        case "-...":
            return "B"
        case "-.-.":
            return "C"
        case "-..":
            return "D"
        case ".":
            return "E"
        case "..-.":
            return "F"
        case "--.":
            return "G"
        case "....":
            return "H"
        case "..":
            return "I"
        case ".---":
            return "J"
        case "-.-":
            return "K"
        case ".-..":
            return "L"
        case "--":
            return "M"
        case "-.":
            return "N"
        case "---":
            return "O"
        case ".--.":
            return "P"
        case "--.-":
            return "Q"
        case ".-.":
            return "R"
        case "...":
            return "S"
        case "-":
            return "T"
        case "..-":
            return "U"
        case "...-":
            return "V"
        case ".--":
            return "W"
        case "-..-":
            return "X"
        case "-.--":
            return "Y"
        case "--..":
            return "Z"
        case ".----":
            return "1"
        case "..---":
            return "2"
        case "...--":
            return "3"
        case "....-":
            return "4"
        case ".....":
            return "5"
        case "-....":
            return "6"
        case "--...":
            return "7"
        case "---..":
            return "8"
        case "----.":
            return "9"
        case "-----":
            return "0"


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
            return "- "
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


def morseCodeGenerator(userChoice, userInput):
    userData = userChoice
    userList = []
    newUserList = []
    finalSplit = []
    if userData == "1":
        userText = userInput
        user_text_to_list = list(userText)
        for letter in user_text_to_list:
            new_list_text = morseEnc(letter.upper())
            userList.append(new_list_text)
        newText = "".join(userList)
        return newText
    else:
        userText = userInput
        print(userText)
        userText_to_list = userText.split('/')
        print(userText_to_list)
        for i, s in enumerate(userText_to_list):
            if " " in s:
                finalSplit.extend(s.split(" "))
                if i != len(userText_to_list) - 1:
                    finalSplit.append("/")
            else:
                finalSplit.append(s)
                if i != len(userText_to_list) - 1:
                    finalSplit.append("/")
            print(finalSplit)
        for letter in finalSplit:
            new_list_text = morseDec(letter)
            newUserList.append(new_list_text)
        newText = "".join(newUserList)
        return newText


@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    if request.method == 'POST':
        text = request.form['input']
        methods = request.form['method']
        result = morseCodeGenerator(userChoice=methods, userInput=text)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
