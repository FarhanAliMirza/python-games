from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager


screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.bgcolor("black")
screen.tracer(0)

player1 = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player1.move_forward, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player1) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player1.is_at_finish_line():
        player1.go_to_start()
        scoreboard.level_up()
        car_manager.level_up()

screen.exitonclick()
