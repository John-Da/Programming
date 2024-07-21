from tkinter import *
import dataBase


def main():
    window = Tk()
    window.geometry('500x500')
    window.title("Testing")

    icon = PhotoImage(file=dataBase.iconImg)
    backgroundImg = PhotoImage(file=dataBase.windowBg)

    window.iconphoto(True, icon)
    window.config(background=dataBase.windowBgColor)

    label = Label(window, image=backgroundImg)
    label.place(relx=0.5, rely=0.5, anchor='center')
    
    
    
    window.mainloop()

