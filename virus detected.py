from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showinfo("Virus Detected", "A virus has been detected in your system. Please take immediate action to remove it.")
button = Button(root, text="Scan for viruses", command=msg)
button.place(x=40, y=80)
root.mainloop()