from turtle import Turtle, Screen
from pong import Pong
screen = Screen()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("The Pong Game")
newPong = Pong()
screen.exitonclick()
