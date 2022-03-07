from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
checkmark = "✔"
checkmark_timer = ""
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global REPS
    global timer
    global checkmark_timer
    REPS = 0
    checkmark_timer = ""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    status_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def check_mark_add():
    global checkmark_timer
    checkmark_timer += f"{checkmark}"
    checkmark_label.config(text=checkmark_timer)

def start_timer():
    global REPS
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if REPS % 2 == 0:
        count_down(work_secs)
        REPS += 1
        status_label.config(text="Work!", fg=GREEN)
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
    elif REPS == 7:
        count_down(long_break_secs)
        REPS = 0
        status_label.config(text="Break.", fg=RED)
        check_mark_add()
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
    elif REPS % 2 != 0:
        count_down(short_break_secs)
        REPS += 1
        status_label.config(text="Take 5!", fg=PINK)
        check_mark_add()
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    min_counter = int(count / 60)
    sec_counter = str(count % 60)
    if len(sec_counter) < 2:
        sec_counter = f"0{sec_counter}"

    canvas.itemconfig(timer_text, text=f"{min_counter}:{sec_counter}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.config(padx=50, pady=25, bg=YELLOW)
window.title("Timer")

# Title Timer label
status_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
status_label.grid(row=0, column=1)

# Tomato picture and timer text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=bg_tomato)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

# Start button
start_button = Button(text="Start", command=start_timer)
start_button.config(padx=2, pady=2)
start_button.grid(row=2, column=0)

# Reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.config(padx=2, pady=2)
reset_button.grid(row=2, column=2)

# Checkmarks
checkmark_label = Label(text="", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3, column=1)

window.mainloop()
