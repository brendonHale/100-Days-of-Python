import turtle as t
import random

def draw_square(turtle):
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)

def dashed_line(turtle):
    for _ in range(50):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_shape(sides, turtle):
    for i in range(3, sides):
        angle = 360 / i
        turtle.color(random_colour())

        for _ in range(i):
            turtle.forward(100)
            turtle.right(angle)

def random_walk(turtle, steps):
    turtle.pensize(15)

    for i in range(steps):
        turtle.color(random_colour())
        turtle.setheading(random.choice(directions))
        turtle.forward(30)

def circles(turtle, gap):
    for _ in range(int(360 / gap)):
        turtle.color(random_colour())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + gap)


timmy = t.Turtle()
screen = t.Screen()
t.colormode(255)
directions = [0, 90, 180, 270]


timmy.shape("turtle")
timmy.color("red")
timmy.speed("fastest")

# draw_square(timmy)
# dashed_line(turtle)
# draw_shape(11, timmy)
# random_walk(timmy, 100)
circles(timmy, 5)

screen.exitonclick()

import heroes
# print(heroes.gen())
