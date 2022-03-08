# Password Generator

# -------------------IMPORTS------------------- #
import random
from tkinter import *
from tkinter import messagebox
import os.path
from random import randint, shuffle, choice
import pyperclip

# -------------------GLOBALS------------------- #
FONT_NAME = "Calibri"
BG_COLOR = "#0072EC"

# -------------------SAVE PASSWORD------------------- #


def add_password(event):

    website = str(website_input.get())
    email = str(email_input.get())
    password = str(password_input.get())

    if not os.path.exists("passwords.txt"):
        passwords_file = open("passwords.txt", "x", encoding='utf-8')
        passwords_file.close()
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Error", message="Please don't leave fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("passwords.txt", "a", encoding='utf-8') as passwords_file:
                passwords_file.write(f"{website} | {email} | {password} \n")
            website_input.delete(0, "end")
            password_input.delete(0, "end")
            website_input.focus()


# -------------------GENERATE PASSWORD------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password_string = "".join(password_list)
    password_input.delete(0, "end")
    password_input.insert(0, string=password_string)
    pyperclip.copy(password_string)

# -------------------GUI------------------- #

# Window setup
window = Tk()
window.config(bg=BG_COLOR, padx=40, pady=40)
window.title("Password Manager")
window.bind("<Return>", add_password)

# Picture Logo
logo_canvas = Canvas(width=375, height=249, highlightthickness=0, bg=BG_COLOR)
logo = PhotoImage(file="logo.png") # Picture size 375x249px
logo_canvas.create_image(188, 125, image=logo)
logo_canvas.grid(row=0, column=0, columnspan=3, padx=0, pady=10)


# Labels
website_label = Label(text="Website:", font=(FONT_NAME, 12, "normal"),bg=BG_COLOR, fg="black")
website_label.grid(row=1, column=0, padx=(5, 5) , pady=2, sticky="E")

email_label = Label(text="Email/Username:", font=(FONT_NAME, 12, "normal"), bg=BG_COLOR, fg="black")
email_label.grid(row=2, column=0, padx=(5, 5), pady=2, sticky="E")

password_label = Label(text="Password:", font=(FONT_NAME, 12, "normal"), bg=BG_COLOR, fg="black")
password_label.grid(row=3, column=0, padx=(5, 5), pady=2, sticky="E")

# Entries/Inputs
website_input = Entry(width=45)
website_input.focus()
# website_input.insert(END, string="Insert website name.")
website_input.grid(row=1, column=1, columnspan=2, padx=(5, 25), pady=5, sticky="W")

email_input = Entry(width=45)
email_input.insert(END, string="cristianmariusv97@gmail.com")
email_input.grid(row=2, column=1, columnspan=2, padx=(5, 25), pady=5, sticky="W")

password_input = Entry(width=22)
# password_input.insert(END, string="Insert password.")
password_input.grid(row=3, column=1, padx=5, pady=5, sticky="W")

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=38)
add_button.bind("<Button-1>", add_password)
add_button.grid(row=4, column=1, columnspan=2, padx=5, pady=10, sticky="W")


window.mainloop()
