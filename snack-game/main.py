# splitting days to build the game (breaking the problems into pieces):
# The plan is to create 3 classes...Snake, Food, Scorecard
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("The Snack Game")
screen.tracer(0)

# Day-1...
# Create a snake
# Move the snake
# Control snake food

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


'''Moving the Snack'''
game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()


# Day-2...
# Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()

# Create a scoreboard
        scoreboard.updatescore()
    scoreboard.score()

# Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_on = False

# Detect collision with tail
#     if head collides with any segment of snake then game over, pass the head segment
    for segment in snake.joint_snake[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()