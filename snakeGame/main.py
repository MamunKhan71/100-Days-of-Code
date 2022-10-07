import time

import pyautogui
from turtle import Turtle, Screen

screen = Screen()
screen.tracer(0)
screen.listen()

screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title("Snake Game")
turtles = []
startPos = [(0, 0), (-20, 0), (-40, 0)]


def turnUp():
    turtles[0].left(90)


def turnDown():
    turtles[0].heading()


for pos in startPos:
    newTurtles = Turtle("square")
    newTurtles.color("white")
    newTurtles.penup()
    newTurtles.goto(pos)
    turtles.append(newTurtles)
gameisOn = True
while gameisOn:
    screen.update()
    time.sleep(.1)
    for ttl_num in range(len(turtles) - 1, 0, -1):
        newXCordX = turtles[ttl_num - 1].xcor()
        newXCordY = turtles[ttl_num - 1].ycor()
        turtles[ttl_num].goto(newXCordX, newXCordY)
    turtles[0].forward(20)
    screen.onkey(fun=turnUp, key="w")
    screen.onkey(fun=turnDown, key="s")
    # screen.onkey(fun=turnLeft, key="w")
screen.exitonclick()
