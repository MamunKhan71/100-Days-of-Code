from turtle import Turtle, Screen

x_pos = 0
y_pos = 0


class Pong:
    def __init__(self):
        self.netBar = []
        self.newPong = Turtle("square")
        self.newPong.color("white")
        self.newPong.goto(0.0, 0.0)
        self.createBar()

    def createBar(self):
        for num in range(3):
            newBar = Turtle("square")
            newBar.color("white")
            newBar.goto()
