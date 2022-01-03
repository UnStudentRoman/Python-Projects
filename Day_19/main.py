# Sketching

from turtle import Turtle, Screen


def move_forward():
    drawing.forward(25)

def move_backward():
    drawing.back(25)

def move_left():
    drawing.left(10)

def move_right():
    drawing.right(10)

def clear_screen():
    drawing.speed(0)
    drawing.setposition(0, 0)
    drawing.setheading(0)
    drawing.clear()
    drawing.speed(8)

drawing = Turtle()
screen = Screen()
drawing.speed(8)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
