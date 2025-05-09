import turtle as T
import random

T.colormode(255)

tony_the_turtle = T.Turtle()
tony_the_turtle.shape("turtle")
tony_the_turtle.color("black", "PaleGreen2")
for i in range(4):
    tony_the_turtle.forward(100)
    tony_the_turtle.right(90)

tony_the_turtle.left(90)

for i in range(15):
    tony_the_turtle.forward(5)
    tony_the_turtle.penup()
    tony_the_turtle.forward(5)
    tony_the_turtle.pendown()

def go_home():
    tony_the_turtle.clear()
    tony_the_turtle.penup()
    tony_the_turtle.home()
    tony_the_turtle.pendown()
    tony_the_turtle.pencolor("black")
go_home()


def random_colour():  
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    tony_the_turtle.pencolor(r,g,b)

def draw(num_sides):
    random_colour()
    for i in range(num_sides):
        angle = 360 / num_sides
        tony_the_turtle.forward(100)
        tony_the_turtle.right(angle)

for i in range(3,9):
    draw(i)



#  Random Walk
go_home()
directions_angles = [0, 90, 180, 270]
def random_direction():
    tony_the_turtle.setheading(random.choice(directions_angles))

tony_the_turtle.pensize(20)
tony_the_turtle.speed("fastest")
for i in range(300):
    random_colour()
    tony_the_turtle.forward(20)
    random_direction()

# Spirograph
go_home()
tony_the_turtle.pensize(1)
def draw_spirograph(set_gap):
    for i in range(int(360 / set_gap)):
        random_colour()
        tony_the_turtle.circle(100)
        heading = tony_the_turtle.heading()
        tony_the_turtle.setheading(heading + set_gap)

draw_spirograph(10)
go_home()
draw_spirograph(5)

screen = T.Screen()
screen.exitonclick()