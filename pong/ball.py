from turtle import Turtle

m_x_distance = 10
m_y_distance = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.x_pos = 0
        self.y_pos = 0
        self.goto(self.x_pos, self.y_pos)

    def move(self):
        global m_x_distance
        global m_y_distance

        self.x_pos += m_x_distance
        self.y_pos += m_y_distance
        if self.y_pos > 280 or self.y_pos < -280 :
            m_y_distance *= -1
        self.goto(self.x_pos, self.y_pos)
