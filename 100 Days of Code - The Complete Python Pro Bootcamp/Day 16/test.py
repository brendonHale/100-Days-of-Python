import another_module
# print(another_module.another_variable)

from turtle import Turtle, Screen
timmy = Turtle()

my_screen = Screen()
timmy.shape("turtle")
timmy.color("DarkOrchid")
timmy.forward(100)
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"])
table.add_column("Type", ["Electric", "Water", "Fire", "Grass"])
table.align = "l"

print(table)