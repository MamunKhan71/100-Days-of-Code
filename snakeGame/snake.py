from turtle import Turtle

STARTPOSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVEDIST = 20


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for pos in STARTPOSITION:
            newTurtles = Turtle("square")
            newTurtles.color("white")
            newTurtles.penup()
            newTurtles.goto(pos)
            self.turtles.append(newTurtles)

    def move(self):
        for ttl_num in range(len(self.turtles) - 1, 0, -1):
            newXCordX = self.turtles[ttl_num - 1].xcor()
            newXCordY = self.turtles[ttl_num - 1].ycor()
            self.turtles[ttl_num].goto(newXCordX, newXCordY)
        self.head.forward(MOVEDIST)

    def up(self):
        self.head.seth(90)

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass
