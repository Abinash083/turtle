from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("purple")
        self.shape("circle")
        self.x_pos = 0
        self.y_pos = 0
        self.goto(self.x_pos, self.y_pos)
        self.m_x_distance = 5
        self.m_y_distance = 5

    def move(self):
        self.x_pos += self.m_x_distance
        self.y_pos += self.m_y_distance
        self.goto(self.x_pos, self.y_pos)

    def back_to_initial(self):
        self.x_pos = 0
        self.y_pos = 0
        self.m_x_distance *= -1


