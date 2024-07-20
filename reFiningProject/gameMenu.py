from tkinter import *
import tkinter
import customtkinter
from PIL import ImageTk, Image
import gameDataAsset





fFamily = gameDataAsset.fFamily
redColor = gameDataAsset.redColor
bgColor = gameDataAsset.bgColor
fgColor = gameDataAsset.fgColor
blueGreen = gameDataAsset.blueGreen
cadetBlue = gameDataAsset.cadetBlue
turquoise = gameDataAsset.turquoise

dataSheet = gameDataAsset.dataSheet
discription = gameDataAsset.gameScript

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

def gameMenu():

    # ------======== Base Frame ========----------
    menuFrm = customtkinter.CTkFrame(master=l1, width=720, height=520, corner_radius=15, fg_color=bgColor)
    menuFrm.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    gameIntro = customtkinter.CTkLabel(master=menuFrm, text="What do you like to play?", font=(fFamily, 38, 'bold'), text_color=redColor)
    gameIntro.place(x=150, y=20)

    def startGame():
        print("Clikced")


    addBtn = customtkinter.CTkButton(master=menuFrm, text="Addition", text_color=bgColor, font=(fFamily, 18, 'bold'), fg_color=blueGreen, hover_color=turquoise, width=110, height=40, command=startGame)
    addBtn.place(x=190, y=180)

    subtBtn = customtkinter.CTkButton(master=menuFrm, text="Subtraction", text_color=bgColor, font=(fFamily, 18, 'bold'), fg_color=blueGreen, hover_color=turquoise, width=110, height=40, command=startGame)
    subtBtn.place(x=420, y=180)

    multBtn = customtkinter.CTkButton(master=menuFrm, text="Multiplication", text_color=bgColor, font=(fFamily, 18, 'bold'), fg_color=blueGreen, hover_color=turquoise, width=110, height=40, command=startGame)
    multBtn.place(x=190, y=280)

    diviBtn = customtkinter.CTkButton(master=menuFrm, text="Division", text_color=bgColor, font=(fFamily, 18, 'bold'), fg_color=blueGreen, hover_color=turquoise, width=110, height=40, command=startGame)
    diviBtn.place(x=420, y=280)

    quitBtn = customtkinter.CTkButton(master=menuFrm, text="Quit", text_color=bgColor, font=(fFamily, 18, 'bold'), fg_color=blueGreen, hover_color=turquoise, width=110, height=40, command=app.quit)
    quitBtn.place(x=300, y=380)



gameMenu()
app.mainloop()