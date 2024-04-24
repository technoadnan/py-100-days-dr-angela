import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.tolist()
num_st_correct = 0


def turtle_operation(x,y,name):
    t = turtle.Turtle()
    t.shape(image)
    t.penup()
    t.hideturtle()
    t.goto(x,y)
    t.write(name)

while num_st_correct < len(all_states):
    ans_st = screen.textinput(f"Guess the state{num_st_correct}/50", prompt="What's another state's name: ").title()

    if ans_st == "Exit":
        break
    if ans_st in all_states:
        num_st_correct += 1
        all_states.remove(ans_st)
        x_axis = int(data[data.state == ans_st].x.item())
        y_axis = int(data[data.state == ans_st].y.item())
        turtle_operation(x_axis, y_axis, ans_st)


data_dict = {
    "states" : all_states
}

pd.DataFrame(data_dict).to_csv("states_to_remember.csv")

screen.mainloop()
