from turtle import Turtle


class PongBall:
    def __init__(self):
        self.newPong = Turtle("square")
        self.newPong.color("white")
        self.newPong.goto(0.0, 0.0)
        self.pongMover()

    def pongMover(self):
        gameOn = True
        while gameOn:
            x = 0
            y = 0
            self.newPong.goto(x=x, y=y)
            x += 20
            if self.newPong.xcor() >= 350:
                while self.newPong.xcor() != 0:
                    x -= 20
                    self.newPong.goto(x=x, y=y)
