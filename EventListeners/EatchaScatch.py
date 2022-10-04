from turtle import Turtle, Screen

jenny = Turtle()
screen = Screen()
headings = 0
jenny.pensize(3)


def move_forward():
    jenny.forward(10)


def move_backward():
    jenny.backward(10)


def move_clockwise():
    global headings
    headings += 10
    jenny.seth(headings)
    if headings == 360:
        headings = 0


def clearScreen():
    global headings
    headings = 0
    jenny.clear()
    jenny.penup()
    jenny.home()
    jenny.pendown()


def move_counterClock():
    global headings
    headings -= 10
    jenny.seth(headings)

    if headings == -360:
        headings = 0


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_clockwise)
screen.onkey(key="d", fun=move_counterClock)
screen.onkey(key="c", fun=clearScreen)
screen.exitonclick()
