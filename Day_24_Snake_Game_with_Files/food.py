from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(.5,.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randrange(-280, 280)
        random_y = random.randrange(-280, 280)
        self.goto(random_x, random_y)