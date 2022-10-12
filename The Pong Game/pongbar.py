from turtle import Turtle


class PongBar(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos)

    def barUp(self):
        yUp = self.ycor() + 20
        self.goto(self.xcor(), yUp)

    def barDown(self):
        yDwn = self.ycor() - 20
        self.goto(self.xcor(), yDwn)