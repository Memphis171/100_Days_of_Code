import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .25
SHORT_BREAK_MIN = .25
LONG_BREAK_MIN = .20
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    counter_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
reps = 0
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        title_label.config(text=f"Work Session", fg=GREEN)
    elif reps %8 == 0:
        count_down(long_break_sec)
        title_label.config(text=f"Long Break Session", fg=RED)
    else:
        count_down(short_break_sec)
        title_label.config(text=f"Short Break Session", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark = mark + "✓"
        counter_label.config(text=mark, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=600, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(300, 112, image = tomato_img)

timer_text = canvas.create_text(300, 130, text="00:00", fill = "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = tk.Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

start_button = tk.Button(window, text = "start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(window, text = "reset", highlightbackground=YELLOW, highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

counter_label = tk.Label(window, text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
counter_label.grid(column=1, row=3)


window.mainloop()