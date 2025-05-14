from ball import Ball
from paddle import Paddle
from score import Score
import time
from turtle import Screen

game_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")


BOT_X = 350
USER_X = -350

bot_paddle = Paddle(BOT_X)
user_paddle = Paddle(USER_X)
ball = Ball()
score = Score()

direction = "up"
def set_direction():
    global direction
    if bot_paddle.ycor() == 220 and direction == "up":
        direction = "down"
    elif bot_paddle.ycor() == -220 and direction == "down":
        direction = "up"

user_paddle.speed("fastest")
screen.listen()
screen.onkey(user_paddle.up, "Up")
screen.onkey(user_paddle.down, "Down")

while game_on:
    set_direction()

    speed = 0.02
    if direction == "up":
        time.sleep(speed)
        bot_paddle.up()
    if direction == "down":
        time.sleep(speed)
        bot_paddle.down()

    # Ball logic
    ball.move()
    if ball.distance(bot_paddle) < 30 or ball.distance(user_paddle) < 30 or ball.ycor() > 270 or ball.ycor() < -270:
        ball.ricochet()
        ball.move()
        ball.move()

    if ball.xcor() > 360 :
        score.add()
        ball.restart()
    if ball.xcor() < -360:
        ball.restart()


screen.exitonclick()


# Created a screen first
# Created a Paddle class that is inherited from Turtle
# Created bot_paddle from the class Paddle, added logic via providing a direction variable, 
# which is set to up by default but once the bot_paddle reaches 220 on y direction is changed to down,
# until the bot_paddle hits -220 on y, then it is set to up
# Created while game_on loop, which checks/updates the direction and requests bot_paddle to go up or down depending on the direction
# Created user_paddle that is responsive to up and down keys