from food import Food
from score import Score
from snake import Snake
import time
from turtle import Screen

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on = True

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def game_over():
    global game_on
    score.game_over()
    game_on = False

def restart():
    score.reset_score()
    snake.reset()

while game_on:
    screen.update()
    speed = 0.11
    time.sleep(speed)
    snake.move()

    # Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add()
        snake.extend()
    #  Detect collision with the wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        restart()
    
    #  Detect collision with the snake body
    for part in snake.segments[2:]:
        if snake.head.distance(part) < 10:
            restart()
    


screen.exitonclick()