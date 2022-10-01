import turtle
from turtle import Turtle

newTurtle = Turtle()
newTurtle.speed(1)
for _ in range(4):
    newTurtle.right(90)
    newTurtle.forward(100)

turtle.exitonclick()
