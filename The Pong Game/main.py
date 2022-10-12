from turtle import Turtle, Screen
from pong import Pong
import time
from pongball import PongBall
screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("The Pong Game")
pong = PongBall()
newPong = Pong(xPos=370, yPos=0)
newPong2 = Pong(xPos=-370, yPos=0)
isGameOn = True
while isGameOn:
    time.sleep(0.1)
    pong.ballMover()
    screen.update()
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce()

screen.exitonclick()
