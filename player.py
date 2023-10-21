from turtle import Turtle

START_POS = (0,-250)
START_SPEED = 20
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = START_SPEED

        self.setheading(90)
        self.penup()
        self.color("purple")
        self.shape("turtle")
        self.goto(START_POS)


    def move_player(self):
        pos = (self.xcor(),self.ycor() + self.speed)
        self.goto(pos)

    def return_start_pos(self):
        return START_POS

    def increase_speed(self):
        self.speed += 1

    def reset_player(self):
        self.speed = START_SPEED
        self.goto(START_POS)

