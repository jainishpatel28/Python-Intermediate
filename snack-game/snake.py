from turtle import Turtle, Screen
MOVING_SPEED = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:

    def __init__(self):
        self.joint_snake = []
        self.createSnake()
        self.head = self.joint_snake[0]

    def createSnake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)


    def add_snake(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.joint_snake.append(snake)


    def extend(self):
        self.add_snake(self.joint_snake[-1].position())

        # add a new segment to the snake.


    def move(self):
        for snake_num in range(len(self.joint_snake) - 1, 0, -1):
            new_x = self.joint_snake[snake_num - 1].xcor()
            new_y = self.joint_snake[snake_num - 1].ycor()
            self.joint_snake[snake_num].goto(new_x, new_y)
        self.joint_snake[0].forward(MOVING_SPEED)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)