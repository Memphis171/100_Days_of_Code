import turtle
import pandas as pd
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US States Quiz")

screen.addshape(image)
turtle.shape(image)
turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#

score = 0
correct_guesses = []
game_on = True
with open("50_states.csv") as states_file:
    file = pd.read_csv(states_file)
    while game_on:
        answer = screen.textinput(f"{score}/50 States Guessed", "What's another state?")
        if answer.lower() in correct_guesses:
            pass
        elif answer.lower() in file.state.str.lower().values:
            correct_answer = file[answer.lower() == file.state.str.lower()]
            turtle.goto(correct_answer.x.values[0], correct_answer.y.values[0])
            turtle.write(correct_answer.state.values[0])
            score += 1
            correct_guesses.append(answer.lower())
            if score == 50:
                game_on = False
        elif answer.lower() == "exit":
            game_on = False

states_to_learn = []
for state in file.state.str.lower().values:
    if state in correct_guesses:
        pass
    else:
        states_to_learn.append(state)

df = {"State": states_to_learn}
add_data = pd.DataFrame(df)
add_data.to_csv("States_to_Learn.csv", index=False)



screen.exitonclick()