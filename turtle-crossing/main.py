import time
from turtle import Screen, Turtle

import car_manager
import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle-Racing")
screen.tracer(0)

turtle = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move_up, "Up")

score = 0
new_speed = 5
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()

#     detect collision with car
    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

#     detect when turtle reaches other side
    if turtle.detect_collision():
        cars.level_up()
        scoreboard.increase_level()

screen.exitonclick()
