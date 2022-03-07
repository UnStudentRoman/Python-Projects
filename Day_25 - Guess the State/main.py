import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Quiz Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
not_guessed_states = []

while len(guessed_states) < 50:
    # Get user answer
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 States", prompt="Name a state:").title()

    # Get states and transform to list
    states = pandas.read_csv("50_states.csv")
    state_list = states.state.to_list()

    # Check answer and write state name
    if answer_state == "Exit":
        not_guessed_states = [state for state in state_list if state not in guessed_states]
        unmentioned_states = pandas.DataFrame(not_guessed_states)
        unmentioned_states.to_csv("Unmentioned_states.csv")
        break
    elif answer_state in state_list:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        state_details = states[states.state == answer_state]
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(int(state_details.x), int(state_details.y))
        state.write(answer_state)


