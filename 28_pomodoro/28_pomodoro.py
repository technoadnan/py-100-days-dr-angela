# ---------------------------- IMPORTS ------------------------------- #
import math
import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ---------------------------- VARIABLES ------------------------------- # 
reps = 0
work_sessions = [0,2,4,6,8]
upt_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(upt_timer)
    timer.config(text="Timer")
    tick.config(text="")
    canvas.itemconfig(text, text="00:00")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    if reps in work_sessions:
        count_down(WORK_MIN*60)
        timer.config(text="WORK", fg=RED)
    elif reps == 7:
        count_down(LONG_BREAK_MIN*60)
    elif reps not in work_sessions:
        count_down(SHORT_BREAK_MIN*60)
        timer.config(text="BREAK", fg=PINK)
    reps = reps + 1
    print(reps)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
num_t = ""
def count_down(count):
    global reps, num_t
    t = 1

    count_min = math.floor(count/60)
    count_sec = count % 60

    canvas.itemconfig(text,text=f"{count_min:02}:{count_sec:02}")    

    if count > 0:
        global upt_timer
        upt_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps in work_sessions:
            num_t = num_t + ("✅"*t)
            tick.config(text=num_t)
        

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="28_tomato.png")
canvas.create_image(100,112,image=tomato_img)
text = canvas.create_text(100,132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)


timer = tk.Label(text="Timer",font=(FONT_NAME,40,"bold"),foreground=GREEN,background=YELLOW)
timer.grid(column=1,row=0)


btn_start = tk.Button(text="Start",command=start_timer,highlightthickness=0,background=YELLOW,padx=5,pady=2,font=("FONT_NAME",10))
btn_start.grid(column=0,row=2)

btn_reset = tk.Button(text="Stop",command=reset_timer,highlightthickness=0,background=YELLOW,padx=5,pady=2,font=("FONT_NAME",10))
btn_reset.grid(column=2,row=2)


tick = tk.Label(text="",background=YELLOW,foreground=PINK)
tick.grid(column=1,row=3)


# start_timer()

window.mainloop()