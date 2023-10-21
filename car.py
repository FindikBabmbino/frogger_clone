from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.set_up_car()

    def set_up_car(self):
        self.shape("square")
        self.shapesize(stretch_len=3)
        self.color("blue")
        self.speed = self.random_speed()
        self.penup()
        self.goto(self.random_pos())

    def increase_speed(self):
        self.speed += 2

    def detect_collision(self,player,car_list,gamemaneger,scoreboard):
        if self.distance(player) < 25:
            gamemaneger.reset_game(player,car_list,scoreboard)

    def move_car(self):
        if self.xcor() < -250:
            self.goto(self.random_pos())
        pos = (self.xcor() - self.speed,self.ycor())
        self.goto(pos)

    def random_pos(self):
        random_pos = 250, random.randint(-200, 285)
        return random_pos

    def random_speed(self):
        rand_speed = random.randint(5,8)
        return rand_speed
