import turtle
import turtle as tim
import random

colors = ["red", "green", "blue", "yellow", "pink","black","grey"]
directions = [0,90,180,270]
ts = True
t = tim.Turtle()
t.speed("fastest")
t.pensize(10)
while ts:
    t.forward(30)
    t.color(random.choice(colors))
    t.seth(random.choice(directions))

tim.exitonclick()
