from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")

window = Tk()

window.title("Miles/ Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

km_result = Label(text="0")
km_result.grid(row=1, column=1)

km_label = Label(text="km")
km_label.grid(row=1, column=2)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(row=2, column=1)

window.mainloop()