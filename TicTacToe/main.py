import os

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


while True:
    i = 0
    while i < 9:
        print(
            f" {game_file[0][0]} | {game_file[0][1]} | {game_file[0][2]}\n-----------\n {game_file[1][0]} | {game_file[1][1]} | {game_file[1][2]}\n-----------\n {game_file[2][0]} | {game_file[2][1]} | {game_file[2][2]}\n")
        user_input = input("Enter your choice ( 1 to 9 ) : ")
        if i % 2 == 0:
            dataWriters(user_input, usr="0")
            winParam = gameWinningRules(i=game_file, dta="0")

        else:
            dataWriters(user_input, usr="X")
            winParam = gameWinningRules(i=game_file, dta="X")

    if winParam == 1:
        print("You Win")
    else:
        print("You Loose")
