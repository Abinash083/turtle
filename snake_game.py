from snake import Snake
import time
from turtle import Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("SnakeGame")
screen.tracer(0)
game_running = True

snake1= Snake()
while game_running:
    screen.update()
    time.sleep(0.09)
    snake1.move()

screen.exitonclick()
