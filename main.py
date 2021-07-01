import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
MAX_CARS = 35
time_to_sleep = 0.2

player = Player()
scoreboard = Scoreboard()

car_list = []

screen.listen()

screen.onkey(key="Up", fun=player.move_up)

game_is_on = True
while game_is_on:
    screen.update()

    car_list_len = len(car_list)
    # creates a new car if list isn't full
    if car_list_len < MAX_CARS:
        if random.randint(0, 100) % 3 == 0 or car_list_len == 0:
            new_car = CarManager()
            car_list.append(new_car)

    # adds force to all the cars in the list
    for car in car_list:
        car.add_force()
    # removes car from the list if the cord is off screen
    for i, car in enumerate(car_list):
        if car.xcor() < -300:
            car.remove_car()
            removed_car = car_list.pop(i)

    # checks collision with car and player
    for car in car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            car.remove_car()
            car_list = []

    # checks if player has reached the top of the screen
    if player.ycor() > 270:
        print("Next Level")
        scoreboard.current_level += 1
        scoreboard.display_level()
        if scoreboard.current_level > 5:
            MAX_CARS = 40
        elif scoreboard.current_level > 10:
            MAX_CARS = 50

        # remove every car in the list to start a new
        for car in car_list:
            car.remove_car()
        car_list = []
        time_to_sleep *= .9
        player.level_up()
        print(time_to_sleep)

    time.sleep(time_to_sleep)


screen.exitonclick()
