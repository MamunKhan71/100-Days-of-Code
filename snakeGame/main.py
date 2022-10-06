import time

import pyautogui
from turtle import Turtle, Screen

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title("Snake Game")
turtles = []
startPos = [(0, 0), (-20, 0), (-40, 0)]
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
    for ttl in turtles:
        ttl.forward(20)

screen.exitonclick()
