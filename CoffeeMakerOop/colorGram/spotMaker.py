import colorgram
import random
import turtle as trL

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
    for _ in range(noOfDotsEach):
        trL.color(random.choice(colLists))
        trL.dot(dotSize)
        trL.forward(forwardValue)

    trL.seth(90)
    trL.forward(forwardValue)
    trL.seth(180)
    for _ in range(noOfDotsEach):
        trL.forward(forwardValue)
    trL.seth(0)


positionSetter(7, 225, 50)
for _ in range(10):
    dotPrinter(10, 20, 50)

trL.exitonclick()
