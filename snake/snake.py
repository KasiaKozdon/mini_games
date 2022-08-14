from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STARTING_LEN = len(STARTING_POSITIONS)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_len = 0
        # create snake
        self.segments = []
        self.create_snake()
        self.alive = True
        self.head = self.segments[0]

    def create_snake(self):
        [self.add_segment(STARTING_POSITIONS[idx]) for idx in range(STARTING_LEN)]

    def move(self):
        for segment in range(self.snake_len - 1, 0, -1):
            self.segments[segment].setpos(self.segments[segment - 1].pos())
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

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.setpos(position)
        self.segments.append(new_segment)
        self.snake_len += 1

    def extend(self):
        tail_position = self.segments[-1].position()
        self.add_segment(position=tail_position)


    def detect_wall_collision(self):
        if self.head.xcor() > 290 \
                or self.head.xcor() < -295 \
                or self.head.ycor() > 290 \
                or self.head.ycor() < -295:
            self.alive = False

    def detect_self_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                self.alive = False

    def detect_collision(self):
        self.detect_wall_collision()
        self.detect_self_collision()


