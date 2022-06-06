from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count/60)
    count_secs = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_secs < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_secs}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_action()
        marks = ""
        work_sesh = math.floor(reps/2)
        for _ in range(work_sesh):
            marks += "✔"
        label_checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg= YELLOW)
label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Helvetica", 50, "bold" and "italic"))
label_checkmark = Label(fg=GREEN, bg=YELLOW)


def start_action():
    global reps
    reps += 1
    work_secs = WORK_MIN*60
    short_break_secs = SHORT_BREAK_MIN*60
    long_break_secs = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        count_down(long_break_secs)
        label_timer.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        label_timer.config(text="Short Break", fg=PINK)
    else:
        count_down(work_secs)
        label_timer.config(text="Work", fg=GREEN)


def reset_action():
    global timer,reps
    window.after_cancel(timer)
    label_timer.config(text="Timer")
    label_checkmark.config(text="")
    canvas.itemconfig(canvas_text, text=f"00:00")
    reps = 0

button_start = Button(text="Start", highlightthickness=0, command=start_action)
button_reset = Button(text="Reset", highlightthickness=0, command=reset_action)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 132, text="00:00", fill="white", font=("Helvetica", 30, "bold" and "italic"))

label_timer.grid(row=0, column=1)
canvas.grid(row=1, column=1)
button_start.grid(row=2, column=0)
button_reset.grid(row=2, column=2)
label_checkmark.grid(row=3, column=1)


window.mainloop()