from tkinter import *


def button_click():
    kilometers = input_entry.get()
    miles = float(kilometers)*0.621371
    resul_label.config(text=round(miles, 2))


# Window
window = Tk()
window.title("KMs to Miles Converter")
window.minsize(width=300, height=60)
window.config(padx=20, pady=20)

# Input Kilometers
input_entry = Entry(width=10)
input_entry.grid(column=1, row=0)


# Label
my_label = Label(text="Is equal to", font=("Arial", 12, "normal"))
my_label.grid(column=0, row=1)
my_label.config(pady=5, padx=5)

my_label = Label(text="Kilometers", font=("Arial", 12, "normal"))
my_label.grid(column=2, row=0)
my_label.config(pady=5, padx=5)

my_label = Label(text="Miles", font=("Arial", 12, "normal"))
my_label.grid(column=2, row=1)
my_label.config(pady=5, padx=5)

# Result label

resul_label = Label(text="0", font=("Arial", 12, "normal"))
resul_label.grid(column=1, row=1)
resul_label.config(padx=5, pady=5)

# Button
button = Button(text="Convert", command=button_click)
button.grid(column=1, row=2)

window.mainloop()
