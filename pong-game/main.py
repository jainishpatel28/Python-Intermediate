from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
speed = 20

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        ball.move_speed = 0.1
        scoreboard.left_point()

    #Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_pos()
        ball.move_speed = 0.1
        scoreboard.right_point()

screen.exitonclick()