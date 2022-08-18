import pandas as pd
import turtle

STATES_TO_PRACTICE_FILENAME = "states_to_practice.csv"  # used for writing


def write_state(state_database_entry, font_color="red"):
    new_state = turtle.Turtle()
    new_state.hideturtle()
    new_state.penup()
    new_state.color(font_color)
    new_state.goto(x=int(state_database_entry["x"]), y=int(state_database_entry["y"]))
    new_state.write(state_database_entry["state"], font=('arial', 12, "normal"))


screen = turtle.Screen()
screen.title("U.S. map game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

state_database = pd.read_csv("50_states.csv")
states_guessed = []
states_count = len(state_database)

while len(states_guessed) < states_count:
    user_answer = screen.textinput(title=f"{len(states_guessed)}/{states_count} guessed",
                                   prompt="Name the state.").title().strip(" ")
    if user_answer == "Exit":
        break
    if user_answer in state_database["state"].values and not (user_answer in states_guessed):
        if len(states_guessed) > 0:
            write_state(state_database[state_database["state"] == states_guessed[-1]].squeeze(), "black")
        state_data = state_database[state_database["state"] == user_answer].squeeze()
        write_state(state_data, "red")
        screen.update()
        states_guessed.append(user_answer)


screen.bgcolor("grey")
mask = state_database["state"].isin(states_guessed)
mask = [not x for x in mask]
missed_states = state_database[mask]
missed_states.to_csv(STATES_TO_PRACTICE_FILENAME)
missed_states.apply(write_state, axis=1)
screen.update()
turtle.mainloop()
