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
blueGreen = gameDataAsset.blueGreen
cadetBlue = gameDataAsset.cadetBlue
turquoise = gameDataAsset.turquoise

dataSheet = gameDataAsset.dataSheet
discription = gameDataAsset.gameScript

bgImg = gameDataAsset.bgImg
gogImg = gameDataAsset.gogImg
fbImg = gameDataAsset.fbImg
resumeImg = gameDataAsset.resumeImg


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry("800x600")
app.title("Math Game")

bkImg = ImageTk.PhotoImage(Image.open(bgImg))
l1 = customtkinter.CTkLabel(master=app, image=bkImg)
l1.pack()


class Buttons:

    addFrm = customtkinter.CTkFrame(master=l1, width=720, height=520, corner_radius=15, fg_color=bgColor)
    addFrm.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


    totalSocore = 0
    chances = 3
    gameIntro = customtkinter.CTkLabel(master=addFrm, text=("Score: " + str(totalSocore)), font=(fFamily, 28, 'bold'), text_color=redColor)
    gameIntro.place(relx=0.15, rely=0.12, anchor=tkinter.CENTER)

    resumeBtnImg = ImageTk.PhotoImage(Image.open(resumeImg).resize((40, 40), Image.AFFINE))

    resumeBtn = customtkinter.CTkButton(master=addFrm, image=resumeBtnImg, text='', fg_color='transparent', hover=None, width=20, height=20, corner_radius=10)
    resumeBtn.place(relx=0.92, rely=0.1, anchor=tkinter.CENTER)

    randomPlace = []
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.answer = self.randomPlace.append(num1+num2)
        self.randomAns()
        self.randomBtn()

    def randomAns(self):
        while len(self.randomPlace) < 4:
            randomNum = random.randint(1, 10)
            if randomNum not in self.randomPlace:
                self.randomPlace.append(randomNum)
    
    def randomBtn(self):
        random.shuffle(self.randomPlace)


num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
print(Button(num1, num2))
app.mainloop()