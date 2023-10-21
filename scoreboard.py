import os.path
from turtle import Turtle

WRITE_POS = (-200,250)
HIGH_POS = (-170,200)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.write_level()

    def write_level(self):
        self.clear()
        self.goto(WRITE_POS)
        self.write(f"Level: {self.level}",move=True,align="center",font=("courier",15,"normal"))
        self.goto(HIGH_POS)
        self.write(f"High Score: {self.high_score}",move=True,align="center",font=("courier",15,"normal"))

    def reset_score_board(self):
        self.write_high_score()
        self.write_level()

    def increase_level(self):
        self.level += 1
        self.write_level()

    def write_high_score(self):
        if self.level > self.high_score:
            self.high_score = self.level
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.level = 0

    def get_high_score(self):
        score = 0
        if os.path.exists("high_score.txt"):
            with open("high_score.txt") as file:
                score = file.read()
        return int(score)