from turtle import Turtle, Screen
from prettytable import PrettyTable, TableStyle

# Day -16 trying out classes in python + a remake of coffee machine project using OOP method

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "green")
timmy.forward(50)

my_screen = Screen()
my_screen.canvheight # attribute
my_screen.exitonclick() # method

print(timmy)
print(my_screen.canvheight)

table = PrettyTable()

table.add_column("Pony Name",["Twilight Sparkle", "Rainbow Dash", "Pinkie Pie", "Rarity", "Flutter Shy", "Apple Jack"])
table.add_column("Pony Race", ["alicorn", "pegasus", "earth pony", "unicorn", "pegasus", "earth pony"])

table.set_style(TableStyle.ORGMODE)
table.align = "l"
print(table)