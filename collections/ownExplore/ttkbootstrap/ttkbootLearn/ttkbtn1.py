from tkinter import *
import ttkbootstrap as tb


# Root
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap")
root.iconbitmap("images/icon.ico")
root.geometry("600x400")


btn_style = tb.Style()
btn_style.configure("success.Outline.TButton", font=("Helvetica", 18))

my_button = tb.Button(
    text="Button", 
    bootstyle="success", 
    style="success.Outline .TButton")
my_button.pack(pady=10)


root.mainloop()
