from turtle import Turtle
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

MOVE_DISTANCE = 20
STARTING_POSITION = (SCREEN_WIDTH/2, 10)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.goto(x=self.xcor() - MOVE_DISTANCE, y=self.ycor())

    def move_right(self):
        self.goto(x=self.xcor() + MOVE_DISTANCE, y=self.ycor())

    def check_road_crossed(self):
        if self.ycor() >= SCREEN_HEIGHT:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False

    def check_car_crash(self, cars):
        """
        :param cars: array of Turtle instances.
        :return: True if distance between self and any car was below the threshold.
        """
        return min([self.distance(car) for car in cars]) < 20





