from turtle import Turtle, Screen

screen = Screen()
screen.tracer(0)


class Pong:
    def __init__(self):
        self.newBar = []
        self.newPong = Turtle("square")
        self.newPong.color("white")
        self.newPong.goto(0.0, 0.0)
        self.createBar()

    def createBar(self):
        x_pos = -380
        y_pos = -20
        for num in range(4):
            newBar = Turtle("square")
            newBar.color("white")
            newBar.penup()
            newBar.setx(x_pos)
            newBar.sety(y_pos)
            self.newBar.append(newBar)
            y_pos += 20
        screen.update()
