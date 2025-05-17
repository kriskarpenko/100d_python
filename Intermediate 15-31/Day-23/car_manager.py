from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.color(random.choice(COLORS))
        self.setheading(180)

        random_position = (random.randint([-250,250]), random.randint([-300,300]))
        self.teleport(random_position)

        self.speed = speed
        speed = STARTING_MOVE_DISTANCE
        
    def move(self,speed):
        self.forward(speed)

    def increase_speed(self):
        speed_increased = self.speed =+ MOVE_INCREMENT
        self.move(speed_increased)
        