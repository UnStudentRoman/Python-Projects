
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

background_screen = Screen()
background_screen.bgcolor("black")
background_screen.setup(800, 600)
background_screen.title("Pong")
background_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
speed = 1

background_screen.onkey(r_paddle.up, "Up")
background_screen.onkey(r_paddle.down, "Down")

background_screen.onkey(l_paddle.up, "w")
background_screen.onkey(l_paddle.down, "s")
background_screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.03333333 / speed)
    background_screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect ball out of bounds right
    if ball.xcor() > 370:
        ball.reset_position()
        score.l_point()
        speed += 0.1

    # Detect ball out of bounds left
    if ball.xcor() < -370:
        ball.reset_position()
        score.r_point()
        speed += 0.1

background_screen.exitonclick()
