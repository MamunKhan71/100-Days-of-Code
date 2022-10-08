from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Arial", 20, "normal"))

    def scoreUpdater(self):
        self.score += 1
