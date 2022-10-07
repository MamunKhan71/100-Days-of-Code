import time
from turtle import Turtle, Screen
from snake import Snake
screen = Screen()
screen.tracer(0)

screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title("Snake Game")
newSnake = Snake()

screen.listen()
screen.onkey(newSnake.up, "up")
screen.onkey(newSnake.down, "down")
screen.onkey(newSnake.left, "left")
screen.onkey(newSnake.right, "right")
gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(.1)
    newSnake.move()


screen.exitonclick()
