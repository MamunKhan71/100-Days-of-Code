from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_left():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_left)
screen.exitonclick()
