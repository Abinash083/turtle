import turtle
from turtle import Turtle, Screen

t1 = Turtle()
screen = Screen()


def move_forward():
    t1.forward(10)


def rotate_left():
    t1.left(10)


def rotate_right():
    t1.right(10)


def move_back():
    t1.forward(-10)


def reset():
    t1.home()
    t1.clear()



screen.listen()
turtle.onkeypress(fun=move_forward, key="w")
turtle.onkeypress(fun=rotate_left, key="a")
turtle.onkeypress(fun=rotate_right,key="d")
turtle.onkeypress(fun=move_back,key="s")
turtle.onkeypress(fun=reset,key="c")

screen.exitonclick()
