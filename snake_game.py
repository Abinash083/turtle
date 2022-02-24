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
start_position_1 = [(-300, 0), (-320, 0), (-340, 0)]
start_position_2 = [(300, 0), (280, 0), (260, 0)]

snake1 = Snake(1, start_position_1)
food1 = Food(-580, -20)
board = Board(-300,280)
snake2 = Snake(2, start_position_2)
food2 = Food(20, 580)
board1 = Board(300, 280)

line = turtle.Turtle("square")
line.shapesize(300, 1)

screen.listen()
screen.onkey(snake1.up, "w")
screen.onkey(snake1.down, "s")
screen.onkey(snake1.left, "a")
screen.onkey(snake1.right, "d")

screen.onkey(snake2.up, "Up")
screen.onkey(snake2.down, "Down")
screen.onkey(snake2.left, "Left")
screen.onkey(snake2.right, "Right")


def food_eating(snake, food, board):
    if snake.head.distance(food) <= 16:
        food.go_to_random_pos()
        board.increase_score()
        snake.increase_snake()


def game_over_condition(snake, board):
    global game_running
    # death by wall touching

    if snake.player == 1:
        boundary_s = -590
        boundary_b = -10
    else:
        boundary_s = 10
        boundary_b = 590
    # for first snake

    if snake.head.xcor() > boundary_b or snake.head.xcor() < boundary_s or \
            snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_running = False
        board.game_over(boundary_s + 300, 0)

    # death by hitting body part
    for part in snake.parts[1:]:
        if snake.head.distance(part) <= 10:
            game_running = False
            board.game_over(boundary_s + 300, 0)


while game_running:
    screen.update()
    time.sleep(0.15)
    snake1.move()
    snake2.move()

    food_eating(snake1, food1, board)
    food_eating(snake2, food2, board1)
    game_over_condition(snake1, board)
    game_over_condition(snake2, board1)

screen.exitonclick()
