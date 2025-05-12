from turtle import Turtle


ALIGNMENT = "center"
FONT_STYLE = ("Arial", 18, "bold")
GAME_OVER_FON_STYLE = ("Arial", 36, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update()
    
    def update(self):
        self.write(f"Score: {self.num}", align=ALIGNMENT, font=FONT_STYLE)

    def add(self):
        self.clear()
        self.num += 1
        self.update()

    def game_over(self):
        self.clear()
        self.teleport(0,0)
        self.color("red")
        self.write(f"Game Over! Your score is: {self.num}",align=ALIGNMENT, font=GAME_OVER_FON_STYLE)