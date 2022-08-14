from turtle import Screen
import time

from food import Food
from scoreboard import Scoreboard
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('~~~Snake~~~')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move snake (always forward)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    snake.detect_collision()
    if not snake.alive:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()