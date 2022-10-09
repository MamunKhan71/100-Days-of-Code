from turtle import Turtle, Screen
from pong import Pong
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
newPong = Pong()
screen.exitonclick()
