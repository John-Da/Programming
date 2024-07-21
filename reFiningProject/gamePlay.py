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


def addGame():
    addFrm = customtkinter.CTkFrame(master=l1, width=720, height=520, corner_radius=15, fg_color=bgColor)
    addFrm.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


    totalSocore = 0
    gameIntro = customtkinter.CTkLabel(master=addFrm, text=f"Score: {totalSocore}", font=(fFamily, 28, 'bold'), text_color=redColor)
    gameIntro.place(relx=0.15, rely=0.12, anchor=tkinter.CENTER)

    resumeBtnImg = ImageTk.PhotoImage(Image.open(resumeImg).resize((40, 40), Image.AFFINE))

    resumeBtn = customtkinter.CTkButton(master=addFrm, image=resumeBtnImg, text='', fg_color='transparent', hover=None, width=20, height=20, corner_radius=10)
    resumeBtn.place(relx=0.92, rely=0.1, anchor=tkinter.CENTER)
    # while True:
    #     try:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    #         answer = num1 + num2

    questionLabel = customtkinter.CTkLabel(master=addFrm, text=f'What is', font=(fFamily, 20, 'bold'), text_color=fgColor)
    questionLabel.place(relx=0.13, rely=0.32, anchor=tkinter.CENTER)

    problemLabel = customtkinter.CTkLabel(master=addFrm, text=f'{num1} + {num2} =', font=(fFamily, 28), text_color=fgColor)
    problemLabel.place(relx=0.15, rely=0.42, anchor=tkinter.CENTER)
            
    #         if userAnswer == answer:
    #             print("Correct")
    #         else:
    #             print("Wrong. Try again!")

    #     except Exception as e:
    #         print(f'Error: {e}')



addGame()
app.mainloop()