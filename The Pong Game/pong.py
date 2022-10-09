from turtle import Turtle, Screen


class Pong:
    def __init__(self):
        self.createPong()

    def createPong(self):
        newPong = Turtle("square")
        newPong.color("white")
        newPong.goto(0.0, 0.0)
    def createBar(self):
        for num in range(3):
            newBar = Turtle()
            self.