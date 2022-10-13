import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
score = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
carlist = CarManager()
player = Player()
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    carlist.carCreator()
    carlist.carMover()
    screen.onkeypress(fun=player.playerUp, key="Up")
    screen.update()
    for num in carlist.carList:
        if num.distance(player) < 20:
            score.scorePrinter()
            score.gameOver()
            break
        elif player.ycor() > 290:
            score.scoreUpdater()
            player.levelIncr()
            carlist.movementIncr()
screen.exitonclick()