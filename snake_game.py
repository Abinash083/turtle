import turtle

from snake import Snake
import time
from turtle import Screen
from food import Food
from score_board import Board

screen = Screen()
screen.setup(width=1200, height=600)
screen.title("SnakeGame")
screen.tracer(0)
game_running = True

snake1 = Snake(1)
food1 = Food(-580, -20)
board = Board()

line=turtle.Turtle("square")
line.shapesize(300, 1)


screen.listen()
screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")


def food_eating(snake, food, board):
    if snake.head.distance(food) <= 16:
        food.go_to_random_pos()
        board.increase_score()
        snake.increase_snake()


while game_running:
    screen.update()
    time.sleep(0.15)
    snake1.move()

    food_eating(snake1, food1, board)
    # death by wall touching
    if snake1.player == 1:
        boundary_s = -600
        boundary_b = -10
    else:
        boundary_s = 10
        boundary_b = 600
    if snake1.head.xcor() > boundary_b or snake1.head.xcor() < boundary_s or \
            snake1.head.ycor() > 280 or snake1.head.ycor() < -280:
        game_running = False
        board.game_over()

    # death by hitting body part
    for part in snake1.parts[1:]:
        if snake1.head.distance(part) <= 10:
            game_running = False
            board.game_over()

screen.exitonclick()
