import colorgram
import turtle as turtle_module
import random

colours = colorgram.extract("image.jpg",16)
turtle_module.colormode(255)
rgb = []
for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    rgb_item = (r,g,b)
    rgb.append(rgb_item)

    
tonny = turtle_module.Turtle()
tonny.speed("fastest")

tonny.penup()
tonny.hideturtle()
tonny.setheading(225)
tonny.forward(300)
tonny.setheading(0)


number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    random_colour = random.choice(rgb)
    tonny.dot(20,random_colour)
    tonny.forward(50)

    if dot_count % 10 == 0:
        tonny.setheading(90)
        tonny.forward(50)
        tonny.setheading(180)
        tonny.forward(500)
        tonny.setheading(0)



screen = turtle_module.Screen()

screen.exitonclick()