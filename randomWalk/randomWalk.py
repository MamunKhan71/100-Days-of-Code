import turtle
import turtle as tim
import random

colors = ["red", "green", "blue", "yellow", "pink","black"]
directions = [0,90,180,270]
ts = True
t = tim.Turtle()
while ts:
    t.forward(90)
    t
    t.seth(random.choice(directions))

tim.exitonclick()
