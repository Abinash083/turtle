from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("Red")
        self.speed("fastest")
        self.shapesize(0.6, 0.6)
        self.go_to_random_pos()

    def go_to_random_pos(self):
        x = random.randint(-275, 275)
        y = random.randint(-275, 275)
        self.goto(x, y)
