from turtle import Turtle

ALIGNMENT = "center"
FONT = ('arial', 20, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score.txt", mode="r") as file:
            self.highest_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}\t Highest score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt", mode="w") as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.update_scoreboard()
