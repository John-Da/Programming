from tkinter import *
import tkinter
import customtkinter
from PIL import ImageTk, Image
import gameDataAsset
import random





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



def gameAdd():
    totalScore = '0'
    chanceLeft = '3'


    # =====----- Score / Chances -----======

    gameScreen = customtkinter.CTkFrame(master=l1, width=720, height=520, corner_radius=15, fg_color=bgColor)
    gameScreen.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    socreLabel = customtkinter.CTkLabel(master=gameScreen, text=f"Score: {totalScore}", font=(fFamily, 26, 'bold'), text_color=redColor)
    socreLabel.place(x=40, y=20)

    chancesLabel = customtkinter.CTkLabel(master=gameScreen, text=f"Chances: {chanceLeft}", font=(fFamily, 26, 'bold'), text_color=redColor)
    chancesLabel.place(x=476, y=20)
    
    menuBtn = customtkinter.CTkButton(master=gameScreen, text="MENU", text_color=bgColor, font=(fFamily, 12), fg_color='blue', hover=False, width=20, border_color=redColor, border_width=1)
    menuBtn.place(x=650, y=20)
    
    
    # =====----- Questions / Answers / Checker -----======
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    answer = num1 + num2
    
    
    
    
    
    def showScore():
        try:
            # if answer == 
            totalScore = str(int(totalScore) + 1)
            socreLabel.configure(text=f'Score: {totalScore}')

        except Exception as e:
            print('Error:', e)

    def showChance():
        pass


    

gameAdd()
app.mainloop()
