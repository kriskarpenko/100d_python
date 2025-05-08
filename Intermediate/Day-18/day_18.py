from turtle import Turtle, Screen

tony_the_turtle = Turtle()
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

tony_the_turtle.clear()
tony_the_turtle.penup()
tony_the_turtle.home()
tony_the_turtle.pendown()






screen = Screen()
screen.exitonclick()