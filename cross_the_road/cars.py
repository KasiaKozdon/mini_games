from turtle import Turtle
import random

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

BASE_CAR_SPEED = 10
BASE_CAR_COUNT = 7

class Cars(Turtle):
    def __init__(self):
        self.cars = []
        self.car_speed = 3
        self.initialise_cars()

    def random_rgb(self):
        colors = (random.random(), random.random(), random.random())
        return colors

    def initialise_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.color(self.random_rgb())
        new_car.shape("square")
        new_car.setheading(180)
        new_car.turtlesize(stretch_wid=1, stretch_len=3)
        return self.find_car_space(new_car)

    def find_car_space(self, car):
        if len(self.cars) == 0:
            return car
        else:
            times_to_try = 100
            while times_to_try > 0:
                car.goto(x=SCREEN_WIDTH, y=random.randint(40, SCREEN_HEIGHT*0.9))
                if min([car.distance(x) for x in self.cars if x != car]) > 20:
                    return car
                else:
                    times_to_try -= 1
        return None

    def initialise_cars(self):
        nr_cars = BASE_CAR_COUNT
        for _ in range(nr_cars):
            new_car = self.initialise_car()
            if new_car is not None:
                self.cars.append(new_car)
        # offset the cars along the xaxis for the start of the game
        [car.goto(x=car.xcor() - random.randint(0, SCREEN_WIDTH), y=car.ycor()) for car in self.cars]

    def move_cars(self):
        for car in self.cars:
            car.goto(x=car.xcor() - self.car_speed, y=car.ycor())

    def reinitialise_gone_offscreen(self):
        [self.find_car_space(car) for car in self.cars if car.xcor() < 0]

    def update_cars(self):
        self.move_cars()
        self.reinitialise_gone_offscreen()

    def speed_up(self):
        self.car_speed += 1