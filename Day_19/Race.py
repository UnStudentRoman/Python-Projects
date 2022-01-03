# Race

# Importing modules needed --------------------------------------------------------------------------------
from turtle import Turtle, Screen
import random

# Setting up the screen --------------------------------------------------------------------------------
screen = Screen()
screen.setup(500, 400)


# Creating the objects --------------------------------------------------------------------------------
turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for color in colors:
    michael = Turtle(shape="turtle")
    michael.penup()
    michael.color(color)
    michael.goto(x=-240, y=100 - colors.index(color)*40)
    turtles.append(michael)


# Starting bet --------------------------------------------------------------------------------
starting_bet = screen.textinput(title="Place your bet.", prompt="Which turtle will win the race? Enter a color: ")
print(starting_bet)


# Race start --------------------------------------------------------------------------------
if starting_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 230:
            if turtle.pencolor() == starting_bet.lower():
                print(f"The {turtle.pencolor()} turtle won! You win the bet.")
            else:
                print(f"The {turtle.pencolor()} turtle won! You lost the bet.")
            is_race_on = False
            break

screen.exitonclick()
