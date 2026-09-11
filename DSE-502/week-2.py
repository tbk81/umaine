from random import randint
from turtle import Turtle, Screen
import random

screen = Screen()
screen.title("Welcome to the Letter Turtle (I make letters!)")
screen.setup(width=750, height=300)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "coral", "aquamarine", "DeepPink",
          "DarkViolet", "AliceBlue", "bisque", "brown", "burlywood", "CadetBlue", "DarkGoldenrod",
          "DarkSalmon", "DarkRed", "DarkSlateBlue", "DodgerBlue", "firebrick", "fuchsia", "magenta", "MistyRose",
          "OliveDrab", "OrangeRed", "PeachPuff", "PowderBlue", "SpringGreen", "tomato", "thistle1", "YellowGreen"
          ]

class LetterTurtle(Turtle):

    def __init__(self):
        """
        Method attributes that all objects created will inherit. All objects created will have attributes from the
        turtle class as well as the turtle being hidden and a speed set.
        :return: None
        """
        super().__init__()
        self.hideturtle()
        self.speed(10)

    def silent_turtle(self):
        """
        This function puts the pen up and sets the turtle back to the home position (0,0). This standardizes the
        movement between letters.
        :return: None
        """
        self.penup()
        self.home()

    def color_width_picker(self):
        """
        A function to randomize the color and width of the letter.
        :return: None
        """
        self.color(random.choice(COLORS))
        self.width(randint(3, 10))

    def letter_c(self, x, y):
        """
        Draws the letter C starting from the specified coordinates.
        It sets the turtle's state to silent, randomizes the color and pen width,
        and moves to the (x, y) position before drawing a semicircle.

        :param x: The x-coordinate where the letter C drawing starts.
        :type x: float
        :param y: The y-coordinate where the letter C drawing starts.
        :type y: float
        :return: None
        """
        self.silent_turtle()
        self.color_width_picker()
        self.goto(x, y)
        self.pendown()
        self.circle(50, -180)

    def letter_o(self, x, y):
        """
        Draws the letter O starting from the specified coordinates.
        It sets the turtle's state to silent, randomizes the color and pen width,
        and moves to the (x, y) position before drawing a circle with a radius of 50.

        :param x: The x-coordinate where the center of the 'O' will be drawn.
        :param y: The y-coordinate where the center of the 'O' will be drawn.
        """
        self.silent_turtle()
        self.color_width_picker()
        self.goto(x, y)
        self.pendown()
        self.circle(50)

    def letter_f(self, x, y):
        """
        Draws the letter F starting from the specified coordinates.
        It sets the turtle's state to silent, randomizes the color and pen width,
        and moves to the (x, y) position before drawing a vertical line. It then will draw horizontal lines to
        complete the F.

        :param x: The x-coordinate of the starting position for drawing the
            letter "F".
        :type x: float
        :param y: The y-coordinate of the starting position for drawing the
            letter "F".
        :type y: float
        :return: None
        """
        self.silent_turtle()
        self.color_width_picker()
        self.goto(x, y)
        self.pendown()
        self.left(90)
        self.forward(100)
        self.penup()
        self.right(90)
        y_coord = 50
        for i in range(2):
            self.goto(x, y_coord)
            self.pendown()
            self.forward(50)
            self.penup()
            y_coord -= 50

    def letter_e(self, x, y):
        """
        Draws the letter E starting from the specified coordinates.
        It sets the turtle's state to silent, randomizes the color and pen width,
        and moves to the (x, y) position before drawing a vertical line. It then will draw horizontal lines to
        complete the E.

        :param x: The x-coordinate where the drawing will start.
        :type x: int or float
        :param y: The y-coordinate where the drawing will start.
        :type y: int or float
        """
        self.silent_turtle()
        self.color_width_picker()
        self.goto(x, y)
        self.pendown()
        self.left(90)
        self.forward(100)
        self.penup()
        self.right(90)
        y_coord = 50
        for i in range(3):
            self.goto(x, y_coord)
            self.pendown()
            self.forward(50)
            self.penup()
            y_coord -= 50


# Creates the turtle object
letter_turtle = LetterTurtle()

start_x = -212.5
start_y = -50
# This will loop through the string "coffee" by each character (char).
for char in "coffee":
    # This takes advantage of the getattr() method that will return the method found in the letter_turtle object
    # by using an f string and the current char. It then assigns the draw_letter variable to point to a function.
    draw_letter = getattr(letter_turtle, f"letter_{char}")
    # Once the draw_letter points to a method, the start_x and start_y variables are inputs for the x and y parameters
    # of the method. start_x variable is incremented by 75 pixels to space out the letter.
    draw_letter(start_x, start_y)
    start_x += 75

screen.exitonclick()
