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

# Creating and adding new segment at the end of snake.
    def add_snake(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.joint_snake.append(snake)

# Function to get snake back to starting positiona and start over by keeping the High score as it is...
    def reset(self):
        for seg in self.joint_snake:
            seg.goto(1000, 1000)
        self.joint_snake.clear()
        self.createSnake()
        self.head = self.joint_snake[0]

# Function to add each new segment at very end of tail segment after food.
    def extend(self):
        self.add_snake(self.joint_snake[-1].position())


# Function that will keep moving the snake from head to tail...
    def move(self):
        for snake_num in range(len(self.joint_snake) - 1, 0, -1):
            new_x = self.joint_snake[snake_num - 1].xcor()
            new_y = self.joint_snake[snake_num - 1].ycor()
            self.joint_snake[snake_num].goto(new_x, new_y)
        self.joint_snake[0].forward(MOVING_SPEED)


# Keys commands for snake...
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
