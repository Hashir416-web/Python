from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("100x100")
def handle_press(event):
    print(event.char)
window.bind("<Key>", handle_press)
def handle_click(event):
    print("\nThe button was clicked at")
button = Button(text="Click Me")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()