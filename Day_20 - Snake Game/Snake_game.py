# Snake Game

# Imports
from turtle import Screen
import time
from Snake import Snake
from Food import Food
from scoreboard import Score

# scrn initialisation
scrn = Screen()
scrn.setup(width=600, height=600)
scrn.bgcolor("black")
scrn.title("Snake Game")
scrn.tracer(0)


# Snake creation
new_snake = Snake()
new_food = Food()
scoreboard = Score()

# Controls
scrn.listen()
scrn.onkey(new_snake.up, "Up")
scrn.onkey(new_snake.down, "Down")
scrn.onkey(new_snake.left, "Left")
scrn.onkey(new_snake.right, "Right")


game_is_on = True
while game_is_on:
    scrn.update()
    time.sleep(0.05)
    new_snake.move()

    # Collision with food
    if new_snake.head.distance(new_food) < 20:
        new_food.food_eaten()
        new_snake.add_snake_part()
        scoreboard.score_increase()

    # Collision with wall
    if new_snake.head.xcor() > 280 or new_snake.head.xcor() < -280 \
            or new_snake.head.ycor() > 280 or new_snake.head.ycor() < -280:
        scoreboard.reset_game()
        new_snake.reset_snake()

    # Collision with tail
    for segment in new_snake.snake[1:]:
        if new_snake.head.distance(segment) < 10:
            scoreboard.reset_game()
            new_snake.reset_snake()

scrn.exitonclick()
