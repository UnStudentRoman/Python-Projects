from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.LEVEL = 1

    def create_car(self):
        if randint(1, 6) == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.goto(300, randint(-250, 250))
            new_car.shape("square")
            new_car.resizemode("user")
            new_car.shapesize(1, 2)
            new_car.color(choice(COLORS))
            self.all_cars.append(new_car)

    def move_forward(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*(self.LEVEL-1))

    def increase_speed(self):
        self.LEVEL += 1