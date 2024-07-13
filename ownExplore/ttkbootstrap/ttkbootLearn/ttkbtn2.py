from tkinter import *
import ttkbootstrap as tb

root = tb.Window(title="Combo box", themename="solar")
root.geometry("500x500")


def clicker():
    my_label.config(text=f"You clicked on {my_combo.get()}!")


def click_bind(e):
    my_label.config(text=f"You clicked on {my_combo.get()}!")


my_label = tb.Label(root, text="Hello World", font=("Helvetica", 28))
my_label.pack(pady=20)


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

my_combo = tb.Combobox(root, bootstyle="success", values=days)
my_combo.pack(pady=20)


my_combo.current(0)
my_button = tb.Button(root, text="Click Me", command=clicker, bootstyle="danger")
my_button.pack(pady=20)

my_combo.bind("<<ComboboxSelected>>", click_bind)

root.mainloop()
