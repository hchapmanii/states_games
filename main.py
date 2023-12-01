import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Reads the CVS file through Pandas
state_data = pandas.read_csv("50_states.csv")

# Creates state list
state_list_append = state_data["state"]

# User initial state guess
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

state_list = []

# Creates the list from csv file
for state in state_list_append:
    state_list.append(state)

# Score of correct state guess
state_score = 0

# List of correct state guess
correct_guess = []

game_continue = True
while game_continue:

    def write_state():
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.color("red")
        t.goto(x=state_x, y=state_y)
        t.write(f"{answer_state}")

    def won():
        turtle.penup()
        turtle.color("red")
        turtle.write("You Won. All states guessed")
        turtle.goto(x=state_data.x, y=state_data.y)

    def learn_states():
        df = pandas.DataFrame(state_list)
        df.to_csv("learn_states.csv")


    if answer_state == "Exit":
        learn_states()
        break

    if state_score == 50:
        won()
        game_continue = False
    else:
        # valid_state = False
        if answer_state in state_list:
            print("Found")
            state_info = state_data[state_data.state == answer_state]
            state_x = int(state_info.x.to_string(index=False))
            state_y = int(state_info.y.to_string(index=False))
            # Pandas .item() removes index another solution instead of index=False
            # state_x = state_info.x.item()
            # print(state_x)
            correct_guess.append(answer_state)
            state_score += 1
            state_list.remove(answer_state)
            write_state()
            answer_state = screen.textinput(title=f"{state_score}/50 States Correct",
                                            prompt="What's another state's name?").title()
        else:
            answer_state = screen.textinput(title=f"{state_score}/50 States Correct",
                                            prompt="Guess another state name?").title()

turtle.mainloop()
