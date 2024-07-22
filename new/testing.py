from tkinter import *
import customtkinter as ctk

import dataBase


def main():
    window = Tk()
    window.geometry('500x500')
    window.title("Testing")
    
    icon = PhotoImage(file=dataBase.iconImg)
    backgroundImg = PhotoImage(file=dataBase.windowBg)

    window.iconphoto(True, icon)
    window.config(background=dataBase.windowBgColor)

    backGround = Label(window, image=backgroundImg)
    backGround.place(relx=0.5, rely=0.5, anchor='center')



# -------------------/// Signing Frame ///----------------------
    btnFrm = Frame(window, bg='white')
    btnFrm.place(relx=0.5, rely=0.5, anchor='center')

    Button(btnFrm, text='Btn 1', width=10, height=5).grid(row=0, column=0, padx=10, pady=10)
    Button(btnFrm, text='Btn 2', width=10, height=5).grid(row=1, column=0, padx=10, pady=10)
    Button(btnFrm, text='Btn 3', width=10, height=5).grid(row=0, column=1, padx=10, pady=10)
    Button(btnFrm, text='Btn 4', width=10, height=5).grid(row=1, column=1, padx=10, pady=10)



    
    

    window.mainloop()

