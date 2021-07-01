from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.current_level = 1
        self.penup()
        self.goto(-285, 250)
        self.color("black")
        self.display_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over Level: {self.current_level}", align="center", font=FONT)

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align="left", font=FONT)
