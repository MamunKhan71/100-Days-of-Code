import turtle
import turtle as tim
import random

t = tim.Turtle()
t.speed("fastest")
tim.colormode(255)


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colorTpl = (r, g, b)
    return colorTpl


directions = [0, 90, 180, 270]
ts = True

randomColor()
t.pensize(10)
while ts:
    t.forward(30)
    t.color(randomColor())
    t.seth(random.choice(directions))

tim.exitonclick()
