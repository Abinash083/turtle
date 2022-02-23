from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.pencolor("black")
        self.hideturtle()
        self.goto(0, 280)
        self.write_score()

    def write_score(self):
        self.write(f"Score {self.score}", align="center", font=("arial", 13, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=("Courier'", 16, "bold"))