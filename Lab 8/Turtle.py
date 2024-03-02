#
# ================================================================================
# Noah Mattison     11/17/2023
# Lab 7
# Purpose: Sorting
# References: Jude Vargas, PowerPoint
# ================================================================================

import turtle
import random
import time

# I know im stealing this but hear me out bro


def atLeftEdge(ball, screenwidth):
    if ball.xcor() < -screenwidth / 2:
        return True
    else:
        return False


def atRightEdge(ball, screenwidth):
    if ball.xcor() > screenwidth / 2:
        return True
    else:
        return False


def atTopEdge(ball, screenheight):
    if ball.ycor() > screenheight / 2:
        return True
    else:
        return False


def atBottomEdge(ball, screenheight):
    if ball.ycor() < -screenheight / 2:
        return True
    else:
        return False


def bounceBall(ball, newdirection):
    if newdirection == 'left' or newdirection == 'right':
        newheading = 180 - ball.heading()
    else:
        newheading = 360 - ball.heading()

    return newheading

# haha balls


def createMonkey():
    for angle in range(0, 19000, 50):
        the_turtle = turtle.getturtle()
        the_turtle.penup()
        turtle.register_shape('monkey.gif')
        the_turtle.shape('monkey.gif')
        the_turtle.setheading(angle)
        the_turtle.forward(100)
        the_turtle.speed(15)
        the_turtle.right(50)


def createBalls(num_balls):
    balls = []
    for n in range(0, num_balls):
        new_ball = turtle.Turtle()
        new_ball.shape('turtle')
        new_ball.fillcolor('green')
        new_ball.speed(70)
        new_ball.penup()
        new_ball.setheading(random.randint(1, 359))
        balls.append(new_ball)

    return balls


def main():
    screenwidth = 800
    screenheight = 600
    turtle.setup(screenwidth, screenheight)

    window = turtle.Screen()
    window.title('The Worlds BIGGEST Pixel')

    numseconds = int(input('How long?'))
    numballs = int(input('How balls?'))

    balls = createBalls(numballs)

    starttime = time.time()

    terminate = False

    while not terminate:
        for k in range(0, len(balls)):
            balls[k].forward(15)

            if atLeftEdge(balls[k], screenwidth):
                balls[k].setheading(bounceBall(balls[k], 'right'))
            elif atRightEdge(balls[k], screenwidth):
                balls[k].setheading(bounceBall(balls[k], 'left'))
            elif atTopEdge(balls[k], screenheight):
                balls[k].setheading(bounceBall(balls[k], 'down'))
            elif atBottomEdge(balls[k], screenheight):
                balls[k].setheading(bounceBall(balls[k], 'up'))

            if time.time() - starttime > numseconds:
                terminate = True
    createMonkey()
    turtle.exitonclick()


if __name__ == '__main__':
    main()

