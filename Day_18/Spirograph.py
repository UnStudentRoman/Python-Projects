# Spirograph
import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("triangle")
timmy.pensize(1)
directions = [0, 90, 180, 270]
timmy.speed(0)
turtle.colormode(255)

angle = 3
for i in range(0, int(360/angle)):
    timmy.circle(100)
    timmy.right(angle)
    timmy.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

screen = Screen()
screen.exitonclick()
