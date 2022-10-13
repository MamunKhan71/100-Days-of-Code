from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.carList = []
        self.setX = 300

    def carCreator(self):
        randChance = random.randint(1,6)
        if randChance == 1:
            newCar = Turtle("square")
            newCar.seth(180)
            setY = random.randint(-250, 250)
            newCar.color(random.choice(COLORS))
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            newCar.penup()
            newCar.goto(self.setX, setY)
            self.carList.append(newCar)

    def carMover(self):
        for car in self.carList:
            car.forward(STARTING_MOVE_DISTANCE)