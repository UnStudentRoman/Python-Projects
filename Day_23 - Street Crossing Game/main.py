import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.onkey(player.move_forward, "w")
screen.onkey(player.move_backward, "s")
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")
screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(0.033333333)
    screen.update()

    car_manager.create_car()
    car_manager.move_forward()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

    if player.winning():
        player.reset_level()
        car_manager.increase_speed()
        score.new_level()

screen.exitonclick()
