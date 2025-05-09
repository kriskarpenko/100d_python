import turtle as turtle_module

tonny = turtle_module.Turtle()
screen = turtle_module.Screen()

def move_forward():
    tonny.forward(10)

def move_backward():
    tonny.backward(10)


def turn_left():
    tonny.left(10)


def turn_right():
    tonny.right(10)

def clean():
    tonny.clear()
    tonny.teleport(0,0)
    tonny.setheading(0)

screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = turn_left)
screen.onkey(key = "d", fun = turn_right)
screen.onkey(key = "c", fun = clean)

screen.exitonclick()