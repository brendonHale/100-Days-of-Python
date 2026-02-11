import random
import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

EMAIL = "scuba_steve@imawesome.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(tite="Oops", message="Please make sure you haven't left any fields empty")

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                          f"Email: {email}\n"
                                                          f"Password: {password}\n"
                                                          f"Is it ok to save?")

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
label_website = Label(text="Website:")
label_website.grid(row=1, column=0, sticky=E)
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0, sticky=E)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0, sticky=E)

# Entries
entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2, pady=2, sticky="EW")
entry_website.focus()

entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2,pady=2, sticky="EW")
entry_email.insert(END, EMAIL)

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1, pady=2, sticky="EW")

# Buttons
button_password = Button(text="Generate Password", command=generate_password)
button_password.grid(row=3, column=2, pady=2, sticky="EW")
button_add = Button(text="Add", width=35, command=save)
button_add.grid(row=4, column=1, columnspan=2, pady=2, sticky="EW")


window.mainloop()