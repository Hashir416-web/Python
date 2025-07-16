from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Fix image import

# Main window setup
root = Tk()
root.title("Crazy Project")
root.config(bg="lightblue")
root.geometry("650x400")

# Load and place image
upload = Image.open("bg.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="lightblue")
label.place(x=180, y=20)

# Welcome text
label1 = Label(root, text="Welcome to Crazy Project", font=("Arial", 20), bg="lightblue")
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to open top-level window
def topwindow():
    top = Toplevel()
    top.title("Crazy Project - Details")
    top.geometry("600x350+50+50")
    top.config(bg="Grey")

    label = Label(top, text="Enter total amount", bg='Light Grey')
    entry_field = Entry(top)

    lbl = Label(top, text="Here are the amount of notes for each denomination", bg='Light Grey')

    l1 = Label(top, text="2000: ", bg='Light Grey')
    l2 = Label(top, text="500: ", bg='Light Grey')
    l3 = Label(top, text="100: ", bg='Light Grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculate():
        try:
            amount = int(entry_field.get())

            notes_2000 = amount // 2000
            amount %= 2000

            notes_500 = amount // 500
            amount %= 500

            notes_100 = amount // 100
            amount %= 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(0, str(notes_2000))
            t2.insert(0, str(notes_500))
            t3.insert(0, str(notes_100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    btn = Button(top, text="Calculate", command=calculate, bg='Brown', fg='White')

    # Placing widgets
    label.place(x=230, y=50)
    entry_field.place(x=200, y=80)
    btn.place(x=240, y=120)

    lbl.place(x=140, y=170)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

# Function for message box and opening topwindow
def message():
    MsgBox = messagebox.showinfo("Crazy Project", "This is a crazy project made with Python and Tkinter!")
    if MsgBox == "ok" or MsgBox == "OK":  # Handles both string cases
        topwindow()

# Start button
button1 = Button(root, text="Let's get started", command=message, bg='Brown', fg='White')
button1.place(x=260, y=360)

root.mainloop()