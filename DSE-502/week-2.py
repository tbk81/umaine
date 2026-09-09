from turtle import *

screen = Screen()
screen.setup(width=750, height=750)

def move_turtle():
    penup()
    hideturtle()

def draw_square():
    move_turtle()
    goto(x=-250, y=200)
    pendown()
    for i in range(4):
        forward(100)
        left(90)


def draw_rectangle():
    move_turtle()
    goto(x=-100, y=200)
    pendown()
    for i in range(2):
        forward(200)
        left(90)
        forward(100)
        left(90)


def draw_triangle():
    move_turtle()
    goto(x=150, y=200)
    pendown()
    for i in range(3):
        forward(100)
        left(120)


def draw_A():
    color('red')
    width(5)
    move_turtle()
    goto(x=100, y=0)
    pendown()
    left(120)
    forward(200)
    left(120)
    forward(200)
    right(180)
    forward(100)
    right(60)
    forward(100)


draw_square()
draw_rectangle()
draw_triangle()
draw_A()

screen.exitonclick()


