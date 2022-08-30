# Based on day 28 task in "100 Days of Code" by Dr. Angela Yu

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

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 224

session_nr = 0
timer = None
timer_default = "00:00"
label_default = "Timer"


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global session_nr
    if timer is not None:
        window.after_cancel(timer)
    session_nr = 0
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    title_label.config(text=label_default)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global session_nr
    session_nr += 1
    sec_per_min = 60
    short_break = SHORT_BREAK_MIN * sec_per_min
    long_break = LONG_BREAK_MIN * sec_per_min
    work = WORK_MIN * sec_per_min
    if session_nr % 8 == 0:
        session_duration = long_break
        title_label.config(text="Long break", fg=RED)
    elif session_nr % 2 == 0:
        session_duration = short_break
        title_label.config(text="Short break", fg=PINK)
    else:
        session_duration = work
        title_label.config(text="Work", fg=GREEN)
    count_down(session_duration)


def split_time(seconds):
    sec_per_min = 60
    min = int(seconds / sec_per_min)
    sec = seconds % sec_per_min
    padding = ""
    if sec < 10:
        padding = "0"
    return f"{min}:{padding}{sec}"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global session_nr
    work_sessions = int(session_nr/2)
    padding = ""
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
        canvas.itemconfig(timer_text, text=split_time(count))
    else:
        check_marks.config(text="✔"*work_sessions)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
background_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=background_image)
timer_text = canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT*0.56, text=timer_default, fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label = tk.Label(text=label_default, fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
title_label.grid(row=0, column=1)

start_button = tk.Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=3, column=0)

reset_button = tk.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=3, column=2)

check_marks = tk.Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(row=4, column=1)

window.mainloop()