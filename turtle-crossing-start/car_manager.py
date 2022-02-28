from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.STARTING_MOVE_DISTANCE = 5

    def create_cars(self):
        num = random.randint(0, 4)
        if num == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(1, 2)
            car.goto(280, random.randint(-250, 250))
            car.setheading(180)
            car.color(random.choice(COLORS))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.STARTING_MOVE_DISTANCE)

    def increase_leve(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT
