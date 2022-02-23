from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, x_min, x_max):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("Red")
        self.speed("fastest")
        self.shapesize(0.6, 0.6)
        self.x_min = x_min
        self.x_max = x_max
        self.go_to_random_pos()

    def go_to_random_pos(self):
        x = random.randint(self.x_min, self.x_max)
        y = random.randint(-275, 275)
        self.goto(x, y)
