from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.LEVEL = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
        self.pendown()
        self.write(f"Level :{self.LEVEL}", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def new_level(self):
        self.clear()
        self.LEVEL += 1
        self.write(f"Level :{self.LEVEL}", font=FONT)
