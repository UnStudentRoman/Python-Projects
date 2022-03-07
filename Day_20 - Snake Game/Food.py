from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.speed(0)
        self.shapesize(0.5)
        self.penup()
        self.goto(x=random.randint(-270, 270), y=random.randint(-270, 270))

    def food_eaten(self):
        self.goto(x=random.randint(-270, 270), y=random.randint(-270, 270))
