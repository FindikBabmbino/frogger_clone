from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from gamemaneger import GameManager
from car import Car
from border import Border
import time



def create_cars():
    cars = []
    for i in range(10):
        car  = Car()
        cars.append(car)
    return cars

def car_funcs(list_of_car,player,gamemaneger,scoreboard):
    for car in list_of_car:
        car.move_car()
        car.detect_collision(player=player,car_list=list_of_car,gamemaneger=gamemaneger,scoreboard=scoreboard)


screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.tracer(0)
screen.title("Frogger Clone")

player = Player()

scoreboard = Scoreboard()

gamemaneger = GameManager()

cars = []

border = Border()

screen.listen()
screen.onkey(player.move_player,"Up")


while True:
    time.sleep(0.1)
    if len(cars) <= 0:
        cars = create_cars()

    car_funcs(cars,player,gamemaneger,scoreboard)
    gamemaneger.check_progress_con(player,scoreboard,cars)

    screen.update()


