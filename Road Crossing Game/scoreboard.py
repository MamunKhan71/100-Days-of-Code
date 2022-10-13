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
        self.write("Game Over", FONT)

    def scorePrinter(self):
        self.goto(x=-270, y=270)
        self.write(f"Level: {self.score}", FONT)

    def scoreUpdater(self):
        self.clear()
        self.score += 1
        self.scorePrinter()
