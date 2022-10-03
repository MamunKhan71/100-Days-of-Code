import colorgram
import random
import turtle as trL
trL.colormode(255)
colList = []
colors = colorgram.extract('image.png', 10)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgbTuple = (r, g, b)
    colList.append(rgbTuple)

colLists = [(239, 243, 246), (243, 236, 241), (211, 136, 119), (42, 21, 13), (2, 14, 24), (12, 97, 149), (241, 217, 82),
            (173, 158, 39)]
trL.color(random.choice(colLists))
trL.dot(15)
trL.

trL.exitonclick()
