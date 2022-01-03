# Random walk
import turtle
from turtle import Turtle, Screen
import random


timmy = Turtle()
timmy.shape("triangle")
timmy.pensize(15)
directions = [0, 90, 180, 270]
timmy.speed(0)
turtle.colormode(255)

for i in range(500):
    timmy.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    timmy.forward(25)
    timmy.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
