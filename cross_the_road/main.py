from turtle import Screen
import time

from player import Player
from scoreboard import Scoreboard
from cars import Cars
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.setworldcoordinates(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Cross the road")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = Cars()
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    cars.update_cars()
    if player.check_road_crossed():
        scoreboard.next_level()
        cars.speed_up()
    if player.check_car_crash(cars.cars):
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
