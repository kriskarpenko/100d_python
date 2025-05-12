from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.color("white")
        self.penup()
        self.teleport(x, 0)
        self.x = x


    def up(self):
        if self.ycor() != 220:
            new_y = self.ycor() + 20
            self.goto(self.x, new_y) 
        
    def down(self):
        if self.ycor() != -220:
            new_y = self.ycor() - 20
            self.goto(self.x, new_y) 


