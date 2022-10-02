import turtle
import random
from turtle import Turtle

randColor = ["black", "yellow", "orange", "red", "blue", "purple", "pink","blue"]
geoTurtle = Turtle()


def shapeDrawer(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        geoTurtle.forward(100)
        geoTurtle.right(angle)


for shape_side in range(3, 11):
    geoTurtle.color(random.choice(randColor))
    shapeDrawer(shape_side)
