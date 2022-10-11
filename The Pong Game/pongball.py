from turtle import Turtle


class PongBall:
    def __init__(self):
        self.newPong = Turtle("circle")
        self.newPong.color("white")
        self.newPong.goto(0.0, 0.0)
        self.newPong.penup()

    def ballMover(self):
        new_x = self.newPong.xcor() + 10
        new_y = self.newPong.ycor() + 10
        self.newPong.goto(new_x, new_y)
