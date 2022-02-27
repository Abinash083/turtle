from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from  scores import Score

screen = Screen()
screen.setup(1000, 600)
screen.title("Pong Game")
screen.bgcolor("beige")
screen.tracer(0)

game_running = True

r_paddle = Paddle("blue", 470)
l_paddle = Paddle("red", -480)
ball = Ball()
l_score = Score(-250, 260, 0)
r_score = Score(250, 260, 0)

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

while game_running:
    screen.update()
    time.sleep(0.03)

    if ball.y_pos > 280 or ball.y_pos < -280:
        ball.m_y_distance *= -1

    # right bounce
    if ball.x_pos == 445 and ball.distance(r_paddle) < 50:
        ball.m_x_distance *= -1
    # left bounce
    if ball.x_pos == -455 and ball.distance(l_paddle) < 50:
        ball.m_x_distance *= -1

    # right miss
    if ball.x_pos > 480:
        ball.back_to_initial()
        l_score.increase_score()

    # left miss
    if ball.x_pos < -480:
        ball.back_to_initial()
        r_score.increase_score()

    ball.move()
screen.exitonclick()
