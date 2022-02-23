from snake import Snake
import time
from turtle import Screen
from food import Food
from score_board import  Board

screen = Screen()
screen.setup(width=600, height=600)
screen.title("SnakeGame")
screen.tracer(0)
game_running = True

snake1 = Snake()
food1 = Food()
board= Board()

screen.listen()
screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")

while game_running:
    screen.update()
    time.sleep(1)
    snake1.move()
    if snake1.head.distance(food1) <= 16:
        food1.go_to_random_pos()
        board.increase_score()

screen.exitonclick()
