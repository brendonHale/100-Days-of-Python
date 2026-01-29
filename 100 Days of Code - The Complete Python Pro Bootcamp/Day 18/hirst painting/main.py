import colorgram
import turtle as turtle_module
import random

# colours = colorgram.extract("image.jpg", 30)
# rgb_colours = []
#
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)

colour_list = [(241, 119, 38), (240, 77, 93), (163, 111, 8), (212, 152, 162), (131, 215, 207), (239, 96, 29), (167, 45, 137), (28, 35, 41), (85, 183, 6), (53, 93, 86), (148, 185, 222), (134, 216, 221), (249, 207, 0), (201, 134, 13), (247, 210, 40), (133, 197, 171), (158, 192, 229), (233, 165, 177), (43, 77, 72), (88, 94, 98), (240, 171, 156), (27, 39, 37), (145, 28, 113), (119, 97, 0), (116, 136, 137)]

turtle_module.colormode(255)
screen = turtle_module.Screen()
tim = turtle_module.Turtle()

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()