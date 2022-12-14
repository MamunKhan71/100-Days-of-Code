from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.scorePrinter()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def scorePrinter(self):
        self.clear()
        self.goto(x=-270, y=250)
        self.write(f"Level: {self.score}", font=FONT)

    def scoreUpdater(self):
        self.score += 1
        self.scorePrinter()
