import turtle as turtle_module
import random

screen = turtle_module.Screen()
screen.setup(width=500,height=400)
game_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a colour:")

all_turtles = []
colours = ["red","orange","yellow","green","blue","indigo"]
y_position = [-100,-70,-40,-10,20,50]

for i in range(6):
    turtle = turtle_module.Turtle(shape="turtle")
    turtle.color(colours[i])
    turtle.teleport(-230, y_position[i])
    all_turtles.append(turtle)



if user_bet:
    game_on = True

while game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_on = False
            winning_colour = turtle.fillcolor()
            if  winning_colour == user_bet:
                print(f'You won. The {winning_colour} was first.')
            else: 
                print(f"You lost. The {winning_colour} was first.")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()