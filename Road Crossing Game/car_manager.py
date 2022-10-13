from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.carList = []
        self.setX = 300
        self.carCreator()

    def carCreator(self):
        newCar = Turtle("square")
        newCar.seth(180)
        for _ in range(6):
            setY = random.randint(-250, 250)
            newCar.color(random.choice(COLORS))
            newCar.shapesize(stretch_wid=2, stretch_len=1)
            newCar.goto(self.setX, setY)
            self.carList.append(newCar)

