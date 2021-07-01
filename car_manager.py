from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=.75, stretch_len=1.5)
        self.create_car()

    def create_car(self):
        random_color = random.choice(COLORS)
        self.color(random_color)
        random_cords = (320, random.randrange(-240, 260))
        self.goto(random_cords)
        self.add_force()

    def add_force(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.setx(new_x)

    def remove_car(self):
        self.ht()
        del self
