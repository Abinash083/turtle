import turtle
import  time
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("SnakeGame")
screen.tracer(0)
start_position = [(0, 0), (-20, 0), (-40, 0)]
parts = []
game_running = True

for pos in start_position:
    part = turtle.Turtle("square")
    part.penup()
    part.goto(pos)
    parts.append(part)

while game_running:
    screen.update()
    time.sleep(0.09)
    for pa in range(len(parts)-1, 0, -1):
        x_cor = parts[pa-1].xcor()
        y_cor = parts[pa-1].ycor()
        parts[pa].goto(x_cor, y_cor)
    parts[0].forward(20)





screen.exitonclick()