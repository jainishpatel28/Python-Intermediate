import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
turtle.colormode(255)
# timmy.shape("turtle")

# to generate the random color
def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return timmy.color(r, g, b)


# Draw a Sqaure
# for rotation in range(4):
#     timmy.forward(100)
#     timmy.left(90)


# Draw a Dahsed Line
# for draw in range(20):
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()


# Drawing different Shapes
# def randomColor():
#     r = random.randint(0, 256)
#     g = random.randint(0, 256)
#     b = random.randint(0, 256)
#     return timmy.color(r, g, b)
#
# for rotation in range(4, 11):
#     turn = 360 / rotation
#     randomColor()
#     for turning in range(rotation):
#         timmy.forward(100)
#         timmy.right(turn)


# Draw/Creating Random walk
# list_of_direction = [90, 180, 270]
# timmy.width(15)
# timmy.speed(5)
# keep_going = True
# while keep_going:
#     timmy.forward(30)
#     randomColor()
#     timmy.setheading(random.choice(list_of_direction))


# Draw circle with same radius and complete the round.(spirograph)
timmy.speed(25)
def draw_spirograph(change_direction):
    for _ in range(int(360 / change_direction)):
        randomColor()
        timmy.setheading(timmy.heading() + change_direction)
        timmy.circle(100)

draw_spirograph(5)





screen = Screen()
screen.exitonclick()