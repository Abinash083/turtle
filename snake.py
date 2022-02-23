from turtle import Turtle

start_position = [(0, 0), (-20, 0), (-40, 0)]
distance = 20
up = 90
left = 180
down = 270
right = 0


class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]
        self.head.color("red")

    def create_snake(self):
        for pos in start_position:
            self.make_snake(pos)

    def make_snake(self, pos):
        part = Turtle("square")
        part.penup()
        part.goto(pos)
        self.parts.append(part)

    def increase_snake(self):
        self.make_snake(self.parts[-1].position())

    def move(self):

        for pa in range(len(self.parts) - 1, 0, -1):
            x_cor = self.parts[pa - 1].xcor()
            y_cor = self.parts[pa - 1].ycor()
            self.parts[pa].goto(x_cor, y_cor)
        self.head.forward(distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
