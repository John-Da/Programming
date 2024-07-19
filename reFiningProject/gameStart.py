from tkinter import *
import tkinter
import customtkinter
from PIL import ImageTk, Image
import gameDataAsset





fFamily = gameDataAsset.fFamily
redColor = gameDataAsset.redColor
bgColor = gameDataAsset.bgColor
fgColor = gameDataAsset.fgColor

dataSheet = gameDataAsset.dataSheet
bgImg = gameDataAsset.bgImg
gogImg = gameDataAsset.gogImg
fbImg = gameDataAsset.fbImg


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry("800x600")
app.title("Math Game")

bkImg = ImageTk.PhotoImage(Image.open(bgImg))
l1 = customtkinter.CTkLabel(master=app, image=bkImg)
l1.pack()



def gameFrame():
    gameScreen = customtkinter.CTkFrame(master=l1, width=720, height=520, corner_radius=15, fg_color=bgColor)
    gameScreen.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    socreLabel = customtkinter.CTkLabel(master=gameScreen, text="SCORE: 00", font=(fFamily, 26, 'bold'), text_color=redColor)
    socreLabel.place(x=40, y=20)

    chancesLabel = customtkinter.CTkLabel(master=gameScreen, text="CHANCES: 0 0 0", font=(fFamily, 26, 'bold'), text_color=redColor)
    chancesLabel.place(x=476, y=20)

    chancesLabel = customtkinter.CTkLabel(master=gameScreen, text="What is :: ", font=(fFamily, 26, 'bold'), text_color=redColor)
    chancesLabel.place(x=30, y=120)

    chancesLabel = customtkinter.CTkLabel(master=gameScreen, text="2 + 1 = ", font=(fFamily, 26, 'bold'), text_color=redColor)
    chancesLabel.place(x=30, y=150)

    chancesLabel = customtkinter.CTkButton(master=gameScreen, text="Option 1", font=(fFamily, 26), text_color=redColor)
    chancesLabel.place(x=406, y=120)

    chancesLabel = customtkinter.CTkButton(master=gameScreen, text="Option 2", font=(fFamily, 26), text_color=redColor)
    chancesLabel.place(x=576, y=120)

    chancesLabel = customtkinter.CTkButton(master=gameScreen, text="Option 3", font=(fFamily, 26), text_color=redColor)
    chancesLabel.place(x=406, y=220)

    chancesLabel = customtkinter.CTkButton(master=gameScreen, text="Option 4", font=(fFamily, 26), text_color=redColor)
    chancesLabel.place(x=576, y=220)






gameFrame()
app.mainloop()
