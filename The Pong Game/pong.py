from turtle import Turtle, Screen

screen = Screen()
screen.tracer(0)


class Pong:
    def __init__(self, xPos, yPos):
        self.x_pos = xPos
        self.y_pos = yPos
        self.newBar = None
        self.newPong = Turtle("square")
        self.newPong.color("white")
        self.newPong.goto(0.0, 0.0)
        self.createBar()

    def createBar(self):
        self.newBar = Turtle("square")
        self.newBar.color("white")
        self.newBar.penup()
        self.newBar.shapesize(stretch_wid=5, stretch_len=1)
        self.newBar.goto(self.x_pos, self.y_pos)
        screen.update()
        self.barMover()

    def barMover(self):
        screen.listen()
        if self.x_pos < 0:
            screen.onkey(fun=self.barUp, key="w")
            screen.onkey(fun=self.barDown, key="s")
        else:
            screen.onkey(fun=self.barUp, key="Up")
            screen.onkey(fun=self.barDown, key="Down")

    def barUp(self):
        self.y_pos = self.y_pos + 20
        self.newBar.goto(x=self.x_pos, y=self.y_pos)
        screen.update()

    def barDown(self):
        self.y_pos = self.y_pos - 20
        self.newBar.goto(x=self.x_pos, y=self.y_pos)
        screen.update()
