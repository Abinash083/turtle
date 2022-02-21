import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=400)

all_turtles = []
is_there_winner = True
colors=["red","blue","green"]





choice = screen.textinput(title="Let the game begin", prompt="which turtle do you want  to bet on R/G/B: ")

for i in (-1, 0, 1):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i+1])
    new_turtle.goto(x=-390, y=100*i)
    all_turtles.append(new_turtle)

while is_there_winner:
    for s_turtle in all_turtles:
        speed=random.randrange(1,15,2)
        s_turtle.forward(speed)
        if s_turtle.xcor() > 375:
            is_there_winner= False
            winner=s_turtle.pencolor()
            print(f"winner is {winner}")


screen.exitonclick()