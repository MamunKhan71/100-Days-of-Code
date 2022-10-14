with open("score.txt", "r") as file:
    content = file.read()
    print(content)
with open("score.txt", "w") as fileW:
    if int(content) < 5:
        fileW.write("5")
