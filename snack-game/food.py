import random
from turtle import Turtle

class Food(Turtle):
    '''whenver the object created from this class will get called it will create new food,
       so only creating __init__ does not really makes much of the difference.'''
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_path = random.randint(-280, 280)
        y_path = random.randint(-280, 280)
        self.goto(x_path, y_path)