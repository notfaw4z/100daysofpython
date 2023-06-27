from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def calculate():
    num = float(input.get())
    output.config(text=f"{num * 1.60934}")

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)

#Label
miles = Label(text="Miles", font=("Calibri", 12))
miles.grid(column=2, row=0)

text1 = Label(text="is equal to", font=("Calibri", 12))
text1.grid(column=0, row=1)

km = Label(text="Km", font=("Calibri", 12))
km.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

output = Label(text="0", font=("Calibri", 12))
output.grid(column=1, row=1)


window.mainloop()