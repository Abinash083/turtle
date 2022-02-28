from turtle import Turtle


class Board(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.penup()
        self.pencolor("black")
        self.x, self.y = x, y
        self.hideturtle()
        self.goto(self.x, self.y)
        self.write_score()
        self.determide_high_score()

    def write_score(self):
        self.write(f"Score {self.score}", align="center", font=("arial", 13, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self, x, y):
        self.goto(x, y)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=("Courier'", 16, "bold"))
        self.goto(x, y-20)
        self.determide_high_score()
        self.write(f"Highest Score : {self.high_score}", align="center", font=("Courier'", 12, "bold"))

    def determide_high_score(self):
        with open("high_score.txt", mode="r") as file:
            self.high_score = file.read()

        if self.score > int(self.high_score):
            self.high_score = str(self.score)
            with open("high_score.txt", mode="w") as file:
                file.write(self.high_score)