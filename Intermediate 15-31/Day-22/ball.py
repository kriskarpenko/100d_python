from turtle import Turtle
import random
import time

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
ANGLE = 45
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ricochet()

    
    def ricochet(self):
        heading = self.heading()
        new_heading = 180
        if heading == RIGHT:
            new_heading = random.choice([LEFT - ANGLE, LEFT + ANGLE]) 
        elif heading == LEFT:
            new_heading == random.choice([RIGHT - ANGLE, RIGHT + ANGLE]) 
        elif heading == UP:  
            new_heading = random.choice([DOWN + ANGLE, DOWN - ANGLE])
        elif heading == DOWN:
            new_heading = random.choice([UP + ANGLE, UP -  ANGLE])
        elif heading < 180:
            new_heading = heading + random.randint(180, 269)
        elif heading > 180:
            new_heading = heading + random.randint(180, 269) - 360

        print(new_heading)

        self.setheading(new_heading)
    
    def move(self):
        self.forward(20)
    
    def restart(self):
        self.teleport(0,0)
        self.ricochet()
        time.sleep(0.5)
