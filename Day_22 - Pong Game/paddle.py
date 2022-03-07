from turtle import Turtle



class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.setpos(pos)
        self.shape("square")
        self.resizemode("user")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.turtlesize(1, 5)

    def up(self):
        self.forward(30)

    def down(self):
        self.backward(30)
