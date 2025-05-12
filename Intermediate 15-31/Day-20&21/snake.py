import turtle as turtle_module

STARING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARING_POSITIONS:
            self.add_segment(position)
            

    def add_segment(self, position):
        seg_item = turtle_module.Turtle(shape="square")
        seg_item.penup()
        seg_item.color("white")
        seg_item.goto(position)
        self.segments.append(seg_item)

    def extend(self):
        last_position = self.segments[-1].position()
        self.add_segment(last_position)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
                snake_position = self.segments[seg_num - 1].position()
                self.segments[seg_num].goto(snake_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)