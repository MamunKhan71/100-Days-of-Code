from turtle import Turtle


class Pong(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("Square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos)

    def barUp(self):
        newY = self.ycor() + 20
        self.goto(x=self.xcor(), y=newY)

    def barDown(self):
        self.y_pos = self.y_pos - 20
        self.newBar.goto(x=self.x_pos, y=self.y_pos)
        screen.update()
