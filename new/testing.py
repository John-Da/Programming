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

    Button(btnFrm, text='Btn 1').pack(side='top')
    Button(btnFrm, text='Btn 2').pack(side='left')
    Button(btnFrm, text='Btn 3').pack(side='bottom')
    Button(btnFrm, text='Btn 4').pack(side='bottom-left')



    
    

    window.mainloop()

