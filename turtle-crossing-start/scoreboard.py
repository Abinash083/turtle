from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(5, 260)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=self.score, font=FONT)

    def increase_score(self):
        self.score += 10
        self.write_score()
