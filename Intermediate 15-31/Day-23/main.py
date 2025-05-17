import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

is_on = True
while is_on:
    speed = 0.1
    time.sleep(speed)
    screen.update()


