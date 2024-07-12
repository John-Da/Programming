from tkinter import *
from tkinter.ttk import *

import tkinter as tk


window = tk.Tk()



frame1 = tk.Frame(
    master=window,
    width=500,
    height=100,
    bg="blue",
)
frame2 = tk.Frame(
    master=window,
    width=100,
    height=100,
    bg="red",
)
frame3 = tk.Frame(
    master=window,
    width=100,
    height=100,
    bg="yellow",
)


hello_title = tk.Label(
    master=frame1,
    text='Welcome to\nMath Speed Game',
    fg='white',
    bg='blue'
)

play_btn = Button(
    master=frame3, 
    padding=10, 
    text='Play', 
    width=10
)

# frame1.pack(fill=tk.BOTH,side=tk.LEFT, expand=True)

frame1.pack(fill=tk.BOTH, expand=True)
frame2.pack(fill=tk.BOTH, expand=True)
frame3.pack(fill=tk.BOTH, expand=True)

hello_title.place(x=190, y=30)
play_btn.place(x=170, y=30)

# greeting = tk.Label(
#     text="Welcome to\nMath Speed Game", 
#     fg="red", 
#     bg="black", 
#     width=60, 
#     height=30
# ).pack()


# entry = tk.Entry(fg="yellow", bg="blue", width=50)
# entry.pack()
# entry.insert(0, "What is your name?")

# button = tk.Button(
#     text="Play",
#     width=13,
#     height=5,
#     fg="red",
#     border=5,
#     relief=tk.RAISED
# )

# text_box = tk.Text()


# button.pack()
# text_box.pack()

window.mainloop()
window.destroy()
