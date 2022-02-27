from turtle import Turtle


class Score(Turtle):

    def __init__(self, x, y, score):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.hideturtle()
        self.score = score
        self.write_score()

    def write_score(self):
        self.write(self.score, align="center", font=("arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()