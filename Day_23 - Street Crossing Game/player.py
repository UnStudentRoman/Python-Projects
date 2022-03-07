from turtle import Turtle
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_level()
        self.setheading(90)

    def move_forward(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def move_backward(self):
        self.sety(self.ycor() - MOVE_DISTANCE)

    def move_left(self):
        self.setx(self.xcor() - MOVE_DISTANCE)

    def move_right(self):
        self.setx(self.xcor() + MOVE_DISTANCE)

    def winning(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_level(self):
        self.goto(STARTING_POSITION)
