import turtle
from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "yellow", "orange", "Black", "grey"]
turtles = []


def turtleCreator():
    for num in range(6):
        newTrtl = Turtle("turtle")
        newTrtl.color(random.choice(colors))
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
turtleCreator()
setPosition()
# userChoice = screen.textinput("Make your bet", "Which turtle color you wanna bet? : ")
# print(userChoice)


screen.exitonclick()
