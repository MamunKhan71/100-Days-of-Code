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
        scoreboards.scoreIncrease()
        newSnake.snake_extend()
    elif newSnake.head.xcor() <= -280 or newSnake.head.xcor() >= 280 or newSnake.head.ycor() <= -280 or newSnake.head.ycor() >= 280:
        screen.clear()
        screen.bgcolor("black")
        scoreboards.gameOver()
        gameIsOn = False
    for seg in newSnake.turtles[1:]:
        if newSnake.head.distance(seg) < 10:
            gameIsOn = False
            screen.clear()
            screen.bgcolor("black")
            scoreboards.gameOver()
screen.exitonclick()
