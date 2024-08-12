from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tbs


icon = "./images/icon.ico"

counter = 0
def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        my_label.config(text='Hello World!')
    else:
        my_label.config(text="Goodbye!")



root = tbs.Window(themename="solar")
# root = Tk()
root.title("TTK Bootstrap")
root.iconbitmap(icon)
root.geometry("500x350")


my_label = tbs.Label(text="Hello World!", font=("Helvetica", 28), bootstyle="default, inverse")
my_label.pack(pady=50)

my_button = tbs.Button(text='Click Me!', bootstyle='primary, outline', command=changer)
my_button.pack(pady=20)

root.mainloop()
