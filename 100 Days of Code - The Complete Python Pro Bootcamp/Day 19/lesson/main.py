from turtle import Turtle, Screen

def move_forwards():
    tim.forward(10)

tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(move_forwards, "space")

screen.exitonclick()