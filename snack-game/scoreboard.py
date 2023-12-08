from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):

     def __init__(self):
         super().__init__()
         self.foodscore = 0
         with open("data.txt") as file:
             self.highscore = int(file.read())
         self.color("white")
         self.hideturtle()
         self.penup()
         self.goto(0, 270)

     def score(self):
         self.clear()
         self.write(f"Score: {self.foodscore} High Score: {self.highscore}", align = ALIGNMENT, font= FONT)

     def reset(self):
         if self.foodscore > int(self.highscore):
             self.highscore = self.foodscore
             with open("data.txt", mode ="w") as file:
                 file.write(f"{self.highscore}")
         self.foodscore = 0

     def updatescore(self):
         self.foodscore += 1
         self.score()
