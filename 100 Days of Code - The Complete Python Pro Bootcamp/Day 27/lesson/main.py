from tkinter import *

def button_clicked():
    my_label.config(text=input.get())

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Button 2", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=30)
input.insert(END, string="Some text to begin with.")
input.grid(column=3, row=2)



window.mainloop()