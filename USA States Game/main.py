import pandas as pd
import turtle

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pd.read_csv("50_states.csv")
score = int(0)
statesList = states["state"].tolist()
answerList = []
while True:
    if score == 0:
        answer = screen.textinput(title="Guess The State", prompt="What's another State?").title()
    else:
        answer = screen.textinput(title=f"{score}/{len(states)} States Correct", prompt="What's another State?").title()
    if answer == "Exit":
        missing_states = []
        for aStates in statesList:
            if aStates not in answerList:
                missing_states.append(aStates)
        data = pd.DataFrame(missing_states)
        data.to_csv("MissingStates")
        print(data)
        break
    if answer in states["state"].values:
        answerList.append(answer)
        usStates = states[states["state"] == answer]
        x = int(usStates["x"])
        y = int(usStates["y"])
        newTurtle = turtle.Turtle()
        newTurtle.penup()
        newTurtle.hideturtle()
        newTurtle.goto(x, y)
        newTurtle.write(answer)
        score += 1
    else:
        continue


