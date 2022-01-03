# Drawing shapes

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(5)
colours = ["cyan", "purple", "snow4", "blue", "red", "OrangeRed", "pearl", "black", "tomato", "orchid"]

def draw_shape(sides):
    for i in range(sides):
        angle = 360 / sides
        timmy.forward(100)
        timmy.right(angle)

for i in range(3,11):
    timmy.color(random.choice(colours))
    draw_shape(i)

screen = Screen()
screen.exitonclick()

