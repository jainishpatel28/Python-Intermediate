# Building Quiz which will ask states name and put in as answer correctly
# Creating main file with turtle and csv file data use
# Moving word as we write to x,y location
# Keeping track of Score

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. Names Game")

# How did I get this two lines,
# apparently, there is no shape like this picture for turtle. So we added that shape in screen, so Turtle can use.
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_names = pandas.read_csv("50_states.csv")
state_name_list = state_names.state.values.tolist()

# somehow keeps this box on for all time to keep asking(use loop for repetition) for state name...
score = 0
answered_guess = []
game_on = True
while game_on:
    player_answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()
    print(player_answer)

# check guess is among 50 states
# and write correct guess on map
    if player_answer == "Exit":
        break
    if player_answer in state_name_list:
        answered_guess.append(player_answer)
        # if answer is correct then, create turtle to write name on X & Y coordinate:
        temp_turtle = turtle.Turtle()
        temp_turtle.hideturtle()
        temp_turtle.penup()

        # now take that entire row of that name and take out the x and y and send turtle to that position
        guess_row = state_names[state_names.state == player_answer]
        temp_turtle.goto(int(guess_row.x), int(guess_row.y))
        temp_turtle.write(player_answer)

        # score tracking
        score += 1


# save missing state in .csv file
missing_state = []
for name in state_name_list:
    if name not in answered_guess:
        missing_state.append(name)

new_data = pandas.DataFrame(missing_state)
new_data.to_csv("state_to_learn.csv")
