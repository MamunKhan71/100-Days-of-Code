import colorgram
import random
import turtle as trL

trL.speed(100)
trL.penup()
trL.colormode(255)
colList = []
colors = colorgram.extract('image.png', 10)
colLists = [(239, 243, 246), (243, 236, 241), (211, 136, 119), (42, 21, 13), (2, 14, 24), (12, 97, 149), (241, 217, 82),
            (173, 158, 39)]


def colorExtractor():
    global colors
    global colList
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgbTuple = (r, g, b)
        colList.append(rgbTuple)


def positionSetter(posValue, headingAngle, forwardValue):
    defaultValue = 0
    for _ in range(posValue):
        trL.seth(headingAngle)
        trL.forward(forwardValue)
    trL.seth(defaultValue)


def dotPrinter(noOfDotsEach, dotSize, forwardValue):
    for dots in range(1, noOfDotsEach + 1):
        print(dots)
        trL.color(random.choice(colLists))
        trL.dot(dotSize)
        trL.forward(forwardValue)
        if dots % 10 == 0:
            trL.seth(90)
            trL.forward(forwardValue)
            trL.seth(180)

            for _ in range(10):
                trL.forward(forwardValue)
            trL.seth(0)
    trL.hideturtle()


positionSetter(7, 225, 50)
dotPrinter(100, 20, 50)
trL.exitonclick()
