from tkinter import *
from datetime import datetime

root = Tk()
root.title("Getting started with widgets")
root.geometry("500x500")

# Widgets
lbl = Label(root, text="Hey there", font=("Arial", 20), fg="purple")

name_lbl = Label(root, text="Enter your name:", font=("Arial", 15))

name_entry = Entry()

text_box = Text(height=5, width=50)  # Moved up so it's created before being used

# Function
def display():
    name = name_entry.get()
    message = "Welcome to the application,\nToday's date is: "
    greet = "Hello " + name + "\n"
    
    text_box.insert(END, greet)
    text_box.insert(END, message + "\n")
    text_box.insert(END, str(datetime.now()) + "\n")

# Button
btn = Button(text="Click me", command=display, font=("Arial", 15), fg="blue")

# Pack widgets
lbl.pack(pady=10)
name_lbl.pack()
name_entry.pack()
btn.pack(pady=10)
text_box.pack(pady=10)
root.mainloop()