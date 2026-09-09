from random import randint
from turtle import Turtle, Screen
import random

screen = Screen()
screen.title("Welcome to the Geometrical (Geo) Turtle")
screen.setup(width=750, height=750)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "coral", "aquamarine", "DeepPink", "DarkViolet"]

class GeoTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(10)

    def silent_turtle(self):
        self.penup()
        self.hideturtle()

    def draw_square(self):
        self.color(random.choice(COLORS))
        self.fillcolor(random.choice(COLORS))
        self.width(randint(1, 8))
        self.silent_turtle()
        self.goto(x=-250, y=200)
        self.pendown()
        self.begin_fill()
        for i in range(4):
            self.forward(100)
            self.left(90)
        self.end_fill()


    def draw_rectangle(self):
        self.color(random.choice(COLORS))
        self.fillcolor(random.choice(COLORS))
        self.width(randint(1, 8))
        self.silent_turtle()
        self.goto(x=-100, y=200)
        self.pendown()
        self.begin_fill()
        for i in range(2):
            self.forward(200)
            self.left(90)
            self.forward(100)
            self.left(90)
        self.end_fill()

    def draw_triangle(self):
        self.color(random.choice(COLORS))
        self.fillcolor(random.choice(COLORS))
        self.width(randint(1, 8))
        self.silent_turtle()
        self.goto(x=150, y=200)
        self.pendown()
        self.begin_fill()
        for i in range(3):
            self.forward(100)
            self.left(120)
        self.end_fill()


    def draw_A(self):
        self.color(random.choice(COLORS))
        self.width(randint(1, 8))
        self.silent_turtle()
        self.goto(x=100, y=0)
        self.pendown()
        self.left(120)
        self.forward(200)
        self.left(120)
        self.forward(200)
        self.goto(x=-50, y=86.6)
        self.left(120)
        self.forward(100)


geoTurtle = GeoTurtle()
geoTurtle.draw_square()
geoTurtle.draw_rectangle()
geoTurtle.draw_triangle()
geoTurtle.draw_A()

screen.exitonclick()


