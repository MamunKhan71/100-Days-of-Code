from turtle import Turtle

STARTPOSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVEDIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for pos in STARTPOSITION:
            self.snake_adder(pos)

    def snake_adder(self, pos):
        newTurtles = Turtle("square")
        newTurtles.color("white")
        newTurtles.penup()
        newTurtles.goto(pos)
        self.turtles.append(newTurtles)

    def snake_extend(self):
        self.snake_adder(self.turtles[-1].position())

    def move(self):
        for ttl_num in range(len(self.turtles) - 1, 0, -1):
            newXCordX = self.turtles[ttl_num - 1].xcor()
            newXCordY = self.turtles[ttl_num - 1].ycor()
            self.turtles[ttl_num].goto(newXCordX, newXCordY)
        self.head.forward(MOVEDIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
