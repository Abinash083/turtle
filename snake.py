from turtle import Turtle, Screen

start_position = [(0, 0), (-20, 0), (-40, 0)]
distance = 20

class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()

    def create_snake(self):
        for pos in self.start_position:
            part = Turtle("square")
            part.penup()
            part.goto(pos)
            self.parts.append(part)

    def move(self):

        for pa in range(len(self.parts) - 1, 0, -1):
            x_cor = self.parts[pa - 1].xcor()
            y_cor = self.parts[pa - 1].ycor()
            self.parts[pa].goto(x_cor, y_cor)
        self.parts[0].forward(distance)
