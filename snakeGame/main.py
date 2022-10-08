import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.tracer(0)
totalScore = 0
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title("Snake Game")
newSnake = Snake()
food = Food()
screen.listen()
scoreboards = Scoreboard()
screen.onkey(newSnake.up, "Up")
screen.onkey(newSnake.down, "Down")
screen.onkey(newSnake.left, "Left")
screen.onkey(newSnake.right, "Right")
gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(.1)
    newSnake.move()
    if newSnake.head.distance(food) < 15:
        food.randPos()

screen.exitonclick()
