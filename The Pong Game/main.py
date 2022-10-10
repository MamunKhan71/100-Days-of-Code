from turtle import Turtle, Screen
from pong import Pong
from pongball import PongBall
screen = Screen()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("The Pong Game")
pong = PongBall()
newPong = Pong(xPos=370, yPos=0)
newPong2 = Pong(xPos=-370, yPos=0)
screen.exitonclick()
