from tkinter import *
import ttkbootstrap as tb


# root
root = tb.Window(title="Testing", themename="solar")
# root.title('Testing')
# root.iconbitmap() #icon
root.geometry("960x800")


# game button function
def startGame():
    pass


# label
game_label = Label(text="Welcome To Testing", font=("Helvetica", 28, "bold"))
game_label.pack(pady=15)


# play button
play_btn = tb.Button(
    bootstyle="success-outline",
    text="Play",
    command=startGame,
    width=15
)
play_btn.pack(pady=50)


root.mainloop()
