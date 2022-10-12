from turtle import Turtle


class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.x_cor = 10
        self.y_cor = 10
        self.shape("circle")
        self.color("white")
        self.goto(0.0, 0.0)
        self.penup()

    def ballMover(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_cor *= -1
