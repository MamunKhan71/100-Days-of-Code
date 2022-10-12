from turtle import Turtle


class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.x_cor = 10
        self.y_cor = 10
        self.shape("circle")
        self.color("white")
        self.penup()

    def ballMover(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    def yBounce(self):
        self.y_cor *= -1

    def xBounce(self):
        self.x_cor *= -1

    def reset(self):
        self.goto(0, 0)
