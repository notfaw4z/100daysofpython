from tkinter import *

def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    my_label["text"] = new_text

window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=20)

#Label
my_label = Label(text="I am a Label", font=("Calibri", 24, "bold"))
my_label["text"] = "New Text"
my_label.grid(column=0, row=0)


#Button
button1 = Button(text="Click me", command=button_clicked)
button1.grid(column=1, row=1)
button1.config(pady=)

button2 = Button(text="Click me", command=button_clicked)
button2.grid(column=3, row=0)


#Entry
input = Entry(width=10)
input.grid(column=4, row=2)



window.mainloop()