print("Welcome to Tic Tac Toe Game")
print("----------------------------")
game_file = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-'],
]


def gameWinningRules(i, dta):
    if (i[0][0] == dta and i[0][1] == dta and i[0][2] == dta) or (
            i[1][0] == dta and i[1][1] == dta and i[1][2] == dta) or \
            (i[2][0] == dta and i[2][1] == dta and i[2][2] == dta) or (
            i[0][0] == dta and i[1][1] == dta and i[2][2] == dta) or \
            (i[0][2] == dta and i[1][1] == dta and i[2][0] == dta) or (
            i[0][0] == dta and i[1][0] == dta and i[2][0] == dta) or \
            (i[0][1] == dta and i[1][1] == dta and i[2][1] == dta) or (
            i[0][2] == dta and i[1][2] == dta and i[2][2] == dta) or \
            (i[0][0] == dta and i[1][0] == dta and i[2][0] == dta) or (
            i[0][1] == dta and i[1][1] == dta and i[2][1] == dta) or \
            (i[0][2] == dta and i[1][2] == dta and i[2][2] == dta):
        return 1
    else:
        return 0


def dataWriters(userInput, usr):
    global game_file
    match userInput:
        case "1":
            game_file[0][0] = usr
        case "2":
            game_file[0][1] = usr
        case "3":
            game_file[0][2] = usr
        case "4":
            game_file[1][0] = usr
        case "5":
            game_file[1][1] = usr
        case "6":
            game_file[1][2] = usr
        case "7":
            game_file[2][0] = usr
        case "8":
            game_file[2][1] = usr
        case "9":
            game_file[2][2] = usr


user = [input("Enter First Player Name (0) : "), input("Enter Second Player Name (X) : ")]
while True:
    i = 0
    while i < 9:
        print(f" {game_file[0][0]} | {game_file[0][1]} | {game_file[0][2]}\n-----------\n {game_file[1][0]} | {game_file[1][1]} | {game_file[1][2]}\n-----------\n {game_file[2][0]} | {game_file[2][1]} | {game_file[2][2]}\n")
        print("Enter your choice from 1 to 9")
        print("------------------------------")
        if i % 2 == 0:
            user_input = input(f"{user[0]}'s Turn : ")
            dataWriters(user_input, usr="0")
            winParam = gameWinningRules(i=game_file, dta="0")
            if winParam == 1:
                print("-------------------------------------")
                print(f"Congratulations!! {user[0]}, You Win")
                print("-------------------------------------")
                exit(0)
            i = i + 1
        else:
            user_input = input(f"{user[1]}'s Turn : ")
            dataWriters(user_input, usr="X")
            winParam = gameWinningRules(i=game_file, dta="X")
            if winParam == 1:
                print("-------------------------------------")
                print(f"Congratulations!! {user[1]}, You Win")
                print("-------------------------------------")
                exit(0)
            i = i + 1
        if i == 9:
            print("Draw")
