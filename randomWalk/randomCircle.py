import turtle as trtl
import random

trtl.colormode(255)
trtl.speed(100)


def circleDrawer(sizeOfSpiral):
    totalLoopRange = round(360/sizeOfSpiral)
    print(totalLoopRange)
    for _ in range(totalLoopRange):
        trtl.color(randomColor())
        trtl.circle(100)
        print(trtl)
        trtl.seth(trtl.heading() + sizeOfSpiral)


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colorTpl = (r, g, b)
    return colorTpl


size_of_gap = int(input("Enter the size of the gap: "))
circleDrawer(size_of_gap)

trtl.exitonclick()
