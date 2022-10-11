from turtle import Turtle


class PongBall:
    def __init__(self):
        self.x_cor = 10
        self.y_cor = 10
        self.newPong = Turtle("circle")
        self.newPong.color("white")
        self.newPong.goto(0.0, 0.0)
        self.newPong.penup()

    def ballMover(self):
        new_x = self.newPong.xcor() + self.x_cor
        new_y = self.newPong.ycor() + self.y_cor
        self.newPong.goto(new_x, new_y)
        if self.newPong.ycor() > 280 or self.newPong.ycor() < -280 :
            self.bounce()

    def bounce(self):
        self.y_cor *= -1

