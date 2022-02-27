from turtle import Turtle, Screen
from paddle import Paddle
import  time

screen = Screen()
screen.setup(1000, 600)
screen.title("Pong Game")
screen.tracer(0)

game_running = True

r_paddle = Paddle(470)
l_paddle = Paddle(-470)

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

while game_running:
    screen.update()
    time.sleep(0.1)
    r_paddle.move()


screen.exitonclick()
