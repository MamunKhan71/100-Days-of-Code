from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.scoreUpdater()

    def scoreUpdater(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Arial", 20, "normal"))

    def scoreIncrease(self):
        self.score += 1
        self.scoreUpdater()
