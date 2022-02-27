from turtle import Turtle

m_distance = 20


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.x_pos = x_pos
        self.y_pos = 0
        self.shapesize(5, 1)
        self.move()

    def up(self):
        if self.y_pos < 260:
            self.y_pos += m_distance

    def down(self):
        if self.y_pos > -260:
            self.y_pos -= m_distance

    def move(self):

        self.goto(self.x_pos, self.y_pos)


