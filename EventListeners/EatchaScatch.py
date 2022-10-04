from turtle import Turtle, Screen

jenny = Turtle()
screen = Screen()


def move_forward():
    jenny.forward(10)


def move_backward():
    jenny.backward(10)


# def move_clockwise():
#
# def move_counterClock():


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_backward)
screen.exitonclick()
