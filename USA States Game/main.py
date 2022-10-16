import pandas as pd
import turtle

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pd.read_csv("50_states.csv")
score = int(1)
answer = screen.textinput(title="Guess The State", prompt="What's another State?").title()
while True:
    answer = screen.textinput(title=f"{score}/{len(states)} States Correct", prompt="What's another State?").title()
    if answer in states["state"].values:
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

screen.mainloop()
