from turtle import Turtle

WRITE_POS = (-200,250)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.color("white")
        self.write_level()

    def write_level(self):
        self.clear()
        self.goto(WRITE_POS)
        self.write(f"Level: {self.level}",move=True,align="center",font=("courier",20,"normal"))


    def write_game_over(self):
        self.goto(0,0)
        self.write("Game Over",move=True,align="center",font=("courier",20,"normal"))

    def increase_level(self):
        self.level += 1
        self.write_level()
