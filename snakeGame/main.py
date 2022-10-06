import pyautogui
from turtle import Turtle,Screen
screen = Screen()
turtles = []
startPos = [(0,0),(-20,0),(-40,0)]
for pos in startPos:
    newTurtles = Turtle("square")
    newTurtles.color("white")
    newTurtles.goto(pos)
    turtles.append(newTurtles)
gameisOn = True
while gameisOn:
    for ttl in turtles:
        ttl.forward(20)

screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.exitonclick()


