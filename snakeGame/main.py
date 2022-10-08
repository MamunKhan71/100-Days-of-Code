import time
from turtle import Turtle, Screen
from snake import Snake
screen = Screen()
screen.tracer(0)

screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title("Snake Game")
newSnake = Snake()

screen.listen()
screen.onkey(newSnake.up, "Up")
screen.onkey(newSnake.down, "Down")
screen.onkey(newSnake.left, "Left")
screen.onkey(newSnake.right, "Right")
gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(.1)
    newSnake.move()


screen.exitonclick()
