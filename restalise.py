import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

class ResturantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.menu_items = {"FRIES MEAL": 2,"LUNCH MEAL": 2,"BURGER MEAL": 3,"PIZZA MEAL": 4,"CHEESE BURGER": 2.5,"DRINKS": 1}
        self.exchange_rate = 82
        self.entries = {}
        self.setup_background(self.root)
        frame = tk.Frame(self.root, bg="white", padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        title = tk.Label(frame, text="Restaurant Order Management", font=("Arial", 16, "bold"), bg="white")
        title.grid(row=0, column=0, columnspan=3, pady=10)
        row_num = 1
        for item, price in self.menu_items.items():
            label = tk.Label(frame, text=f"{item} (${price}):", anchor='w', bg="white")
            label.grid(row=row_num, column=0, sticky="w")
            entry = tk.Entry(frame, width=5)
            entry.insert(0, "0")
            entry.grid(row=row_num, column=1)
            self.entries[item] = entry
            row_num += 1
        currency_label = tk.Label(frame, text="Currency:", bg="white")
        currency_label.grid(row=row_num, column=0, sticky="w", pady=(10, 0))
        self.currency_var = tk.StringVar(value="USD")
        currency_dropdown = ttk.Combobox(frame, textvariable=self.currency_var, values=["USD", "AUD"], state="readonly")
        currency_dropdown.grid(row=row_num, column=1, pady=(10, 0))
        row_num += 1
        order_btn = tk.Button(frame, text="Place Order", command=self.calculate_total)
        order_btn.grid(row=row_num, column=0, columnspan=2, pady=10)

    def setup_background(self, root):
        try:
            image = Image.open("restaurant_bg.jpg")
            image = image.resize((600, 400), Image.ANTIALIAS)
            self.bg_image = ImageTk.PhotoImage(image)
            bg_label = tk.Label(root, image=self.bg_image)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print("Background image failed to load:", e)

    def calculate_total(self):
        total = 0
        try:
            for item, entry in self.entries.items():
                qty = int(entry.get())
                total += qty * self.menu_items[item]
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers only.")
            return
        currency = self.currency_var.get()
        if currency == "INR":
            total *= self.exchange_rate
            currency_symbol = "₹"
        else:
            currency_symbol = "$"
        messagebox.showinfo("Order Summary", f"Total Amount: {currency_symbol}{total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ResturantOrderManagement(root)
    root.mainloop()
