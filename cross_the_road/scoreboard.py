from turtle import Turtle
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=10, y=SCREEN_HEIGHT*0.95)
        self.level = 1
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}", font=('arial', 20, 'bold'), align="left")

    def next_level(self):
        self.level += 1
        self.update_board()

    def game_over(self):
        game_over_notice = Turtle()
        game_over_notice.penup()
        game_over_notice.goto(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
        game_over_notice.write("GAME OVER", font=('arial', 30, 'bold'), align="center")
