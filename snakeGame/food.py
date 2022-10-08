import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.randX = None
        self.randY = None
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.randPos()

    def randPos(self):
        self.randX = random.randint(-270, 270)
        self.randY = random.randint(-270, 270)
        self.goto(self.randX, self.randY)
