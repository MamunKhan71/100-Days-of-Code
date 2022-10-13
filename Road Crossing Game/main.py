import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
carlist = CarManager()
player = Player()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    carlist.carCreator()
    carlist.carMover()
    screen.onkeypress(fun=player.playerUp, key="Up")
    screen.update()
    for num in carlist.carList :
        if num.distance(player) < 20:
            print("Car hits!")
screen.exitonclick()