#
# ================================================================================
# Noah Mattison     12/06/2023
# Lab extra credit
# Purpose: turtle
# References: Jude Vargas
# ================================================================================

import random
import turtle


def drawBox(turt, xpos, ypos, width, height, rgb_tuple):
    """
    Creates a box
    :param turt: instance of a turtle
    :param xpos: x position to draw box
    :param ypos:  y position to draw box
    :return:
    """
    down = turtle.pen()["pendown"]
    turt.penup()
    turt.setpos(xpos, ypos)
    turt.pendown()

    turt.setheading(0)

    turt.fillcolor(rgb_tuple)
    turt.begin_fill()

    turt.forward(width)
    turt.right(90)
    turt.forward(height)
    turt.right(90)
    turt.forward(width)
    turt.right(90)
    turt.forward(height)
    turt.right(90)

    turt.end_fill()

    if not down:
        turt.penup()


def main():
    screenwidth = 800
    screenheight = 600
    turtle.setup(screenwidth, screenheight)
    window = turtle.Screen()
    window.title('Yeehaw')
    window.colormode(255)

    turt = turtle.getturtle()

    # Draws the box for Tiddle man
    drawBox(turt, -100, 100, 200, 200, (138, 150, 90))

    # Sends Tiddles back to the center
    turt.penup()
    turt.setpos(0, 0)
    turt.shape('turtle')
    turt.pensize(5)
    turt.pendown()

    colors = ["red", "orange", "green", "blue", "purple"]
    length = 5

    for count in range(5):
        color = random.choice(colors)
        turt.color(color)
        # Handles the random direction and distance Tiddles moves
        turt.setheading(random.randint(0, 359))
        turt.forward(random.randint(1, 200))

        # checks if outside the box
        if turt.pos()[0] < -100 or turt.pos()[0] > 100 or turt.pos()[1] < -100 or turt.pos()[1] > 100:
            turt.write("Tiddles escaped!")
        else:
            turt.write("Darn")

    # Stops window from instantly closing
    turtle.done()


if __name__ == "__main__":
    main()


