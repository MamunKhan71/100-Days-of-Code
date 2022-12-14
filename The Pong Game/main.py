from turtle import Turtle, Screen
from pongbar import PongBar
import time
from pongball import PongBall
from scoreboard import ScoreBoard
screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("The Pong Game")
pongBall = PongBall()
right_paddle = PongBar((350, 0))
left_paddle = PongBar((-350, 0))

screen.listen()
scores = ScoreBoard()
screen.onkeypress(fun=right_paddle.barUp, key="Up")
screen.onkeypress(fun=right_paddle.barDown, key="Down")
screen.onkeypress(fun=left_paddle.barUp, key="w")
screen.onkeypress(fun=left_paddle.barDown, key="s")
isGameOn = True
while isGameOn:
    time.sleep(pongBall.speeds)
    screen.update()
    pongBall.ballMover()
    if pongBall.ycor() > 280 or pongBall.ycor() < -280:
        pongBall.yBounce()
    if pongBall.distance(right_paddle) < 60 and pongBall.xcor() > 320 or pongBall.distance(left_paddle) < 60 and pongBall.xcor() < -320:
        pongBall.xBounce()

    if pongBall.xcor() > 390:
        scores.lScorePoint()
        pongBall.reset()
        pongBall.xBounce()
    if pongBall.xcor() < -390:
        scores.rScorePoint()
        pongBall.reset()
        pongBall.xBounce()

screen.exitonclick()
