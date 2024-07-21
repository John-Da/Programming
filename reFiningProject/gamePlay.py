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
    gameIntro.place(relx=0.15, rely=0.1, anchor=tkinter.CENTER)

    gameIntro = customtkinter.CTkButton(master=addFrm, text="၊ ၊", font=(fFamily, 28, 'bold'), text_color=bgColor, hover=None, width=10, height=28, corner_radius=10)
    gameIntro.place(relx=0.90, rely=0.1, anchor=tkinter.CENTER)
    # while True:
    #     try:
    #         num1 = random.randint(1, 10)
    #         num2 = random.randint(1, 10)
    #         answer = num1 + num2

    #         print(f'{num1} + {num2} = {answer}')
    #         userAnswer = int(input("Ans: "))
            
    #         if userAnswer == answer:
    #             print("Correct")
    #         else:
    #             print("Wrong. Try again!")

    #     except Exception as e:
    #         print(f'Error: {e}')



addGame()
app.mainloop()