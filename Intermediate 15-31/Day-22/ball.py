from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
    
    def ricochet(self):
        heading = self.heading
        if heading <= 315:
            new_heading = heading() + 45
        else:
            new_heading = (360 - heading()) + 45
        self.setheading(new_heading)
    
    def move(self):
        self.forward(20)