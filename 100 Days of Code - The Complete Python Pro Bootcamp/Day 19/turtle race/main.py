from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which Turtle Do You Bet On? Enter A Colour: ").lower()
colours = ["red", "blue", "green", "yellow", "orange", "purple"]
y_positions = [-75, -45, -15, 15, 45, 75]
turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print("You Win!")
            else:
                print(f"You Lose! The winning turtle is: {winning_colour}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()