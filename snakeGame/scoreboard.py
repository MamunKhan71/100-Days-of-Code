from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


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
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def scoreIncrease(self):
        self.score += 1
        self.scoreUpdater()

    def gameOver(self):
        self.goto(0.00, 0.00)
        self.color("red")
        self.write(arg=f"Game Over!", move=False, align="Center", font=FONT)
        self.finalScore()

    def finalScore(self):
        self.goto(x=.00, y=-30.00)
        self.color("white")
        self.write(arg=f"Final Score - {self.score}", move=False, align="Center", font=FONT)
