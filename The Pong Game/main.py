from turtle import Turtle, Screen
from pongbar import PongBar
import time
from pongball import PongBall

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("The Pong Game")
pongBall = PongBall()
right_paddle = PongBar((350, 0))
left_paddle = PongBar((-350, 0))

screen.listen()
screen.onkey(fun=right_paddle.barUp, key="Up")
screen.onkey(fun=right_paddle.barDown, key="Down")
screen.onkey(fun=left_paddle.barUp, key="w")
screen.onkey(fun=left_paddle.barDown, key="s")

isGameOn = True
while isGameOn:
    time.sleep(0.1)
    screen.update()
    pongBall.ballMover()
    if pongBall.ycor() > 280 or pongBall.ycor() < -280:
        pongBall.bounce()
    if pongBall.distance(right_paddle) < 50 and pongBall.xcor() > 340:
        print("Ball Touched The Bar")
        pongBall.xBounce()
    if pongBall.distance(left_paddle) < 50 and pongBall.xcor() > -340:
        print("Ball Touched The Bar")
        pongBall.xBounce()

screen.exitonclick()