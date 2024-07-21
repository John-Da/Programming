from tkinter import *
import tkinter
import customtkinter
from PIL import ImageTk, Image
import gameDataAsset
# import gameMenu





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
playImg = gameDataAsset.playImg


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry("800x600")
app.title("Math Game")

bkImg = ImageTk.PhotoImage(Image.open(bgImg))
l1 = customtkinter.CTkLabel(master=app, image=bkImg)
l1.pack()

def gameStart():

    # ------======== Base Frame ========----------
    startScreen = customtkinter.CTkFrame(master=l1, width=720, height=520, corner_radius=15, fg_color=bgColor)
    startScreen.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    gameIntro = customtkinter.CTkLabel(master=startScreen, text=f"Welcome to Math Game", font=(fFamily, 38, 'bold'), text_color=redColor)
    gameIntro.place(x=170, y=20)


    # ------======== Script Frame ========----------
    scriptFrm = customtkinter.CTkFrame(master=startScreen, width=660, height=200, corner_radius=15, fg_color=fgColor)
    scriptFrm.place(x=30, y=116)

    with open(discription, 'r') as script:
        readFile = script.read()

    scriptLabel = customtkinter.CTkLabel(master=startScreen, text=readFile, wraplength=580, font=(fFamily, 12), text_color=redColor, bg_color=fgColor)
    scriptLabel.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
# n, ne, e, se, s, sw, w, nw, or center

    def startGame():
        try:
            app.destroy()
            import gameMenu
            gameMenu.gameMenu()
        except Exception as e:
            print(f'Error: {e}')
        pass
    

    playBtnImg = ImageTk.PhotoImage(Image.open(playImg).resize((20, 20), Image.AFFINE))
    startBtn = customtkinter.CTkButton(master=startScreen, image=playBtnImg, text="Start", text_color=bgColor, font=(fFamily, 18, 'bold'), fg_color=blueGreen, hover_color=turquoise, width=110, height=40, compound='left', command=startGame)
    startBtn.place(x=310, y=380)



gameStart()
app.mainloop()