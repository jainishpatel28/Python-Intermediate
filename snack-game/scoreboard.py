from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):

     def __init__(self):
         super().__init__()
         self.foodscore = 0
         self.color("white")
         self.hideturtle()
         self.penup()
         self.goto(0, 270)
         self.updatescore()

     def score(self):
         self.write(f"Score: {self.foodscore}", align = ALIGNMENT, font= FONT)

     def game_over(self):
         self.goto(0, 0)
         self.write("GAME OVER.", align = ALIGNMENT, font= FONT)

     def updatescore(self):
         self.foodscore += 1
         self.clear()
         self.score()