import turtle
from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "yellow", "orange", "Black"]
turtles = []


def turtleCreator():
    for num in range(6):
        newTrtl = Turtle("turtle")
        newTrtl.color(colors[num])
        newTrtl.penup()
        turtles.append(newTrtl)


def setPosition():
    startingPoint = 400 / 6
    setVal = startingPoint/2
    for num in range(6):
        turtles[num].goto(x=-230, y=startingPoint)
        startingPoint -= setVal


screen = Screen()
screen.setup(width=500, height=400)
isRaceOn = False
userChoice = screen.textinput("Make your bet", "Which turtle color you wanna bet? : ").lower()

if userChoice:
    isRaceOn = True
    turtleCreator()
    setPosition()
while isRaceOn:
    for ttRle in turtles:
        if ttRle.xcor() > 230:
            isRaceOn = False
            winningColor = ttRle.pencolor()
            if winningColor == userChoice:
                print(f"Congratulations! You Win! Winner is : {winningColor}")
            else:
                print(f"You Loose! The Winning Turtle is : {winningColor}")
        randomNum = random.randint(1, 10)
        ttRle.forward(randomNum)
screen.exitonclick()
