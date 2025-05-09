from snake import Snake
import time
import turtle as turtle_module

screen = turtle_module.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on = True

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_on:
    screen.update()
    time.sleep(0.13)

    snake.move()

    


screen.exitonclick()