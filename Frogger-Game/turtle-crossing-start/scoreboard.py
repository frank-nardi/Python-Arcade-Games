from turtle import Turtle

FONT = ("Courier", 24, "bold")
LEVEL = 1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.level = LEVEL
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
