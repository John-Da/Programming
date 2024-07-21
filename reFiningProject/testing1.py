

import random
import customtkinter
from PIL import Image, ImageTk
import tkinter
import gameDataAsset

class Buttons:
    def __init__(self, master, num1, num2, bgColor, fFamily, redColor, resumeImg):
        self.master = master
        self.num1 = num1
        self.num2 = num2
        self.bgColor = bgColor
        self.fFamily = fFamily
        self.redColor = redColor
        self.resumeImg = resumeImg
        
        self.addFrm = customtkinter.CTkFrame(master=master, width=720, height=520, corner_radius=15, fg_color=bgColor)
        self.addFrm.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.totalScore = 0
        self.gameIntro = customtkinter.CTkLabel(master=self.addFrm, text=f"Score: {self.totalScore}", font=(fFamily, 28, 'bold'), text_color=redColor)
        self.gameIntro.place(relx=0.15, rely=0.12, anchor=tkinter.CENTER)

        resumeBtnImg = ImageTk.PhotoImage(Image.open(resumeImg).resize((40, 40), Image.AFFINE))
        self.resumeBtn = customtkinter.CTkButton(master=self.addFrm, image=resumeBtnImg, text='', fg_color='transparent', hover=None, width=20, height=20, corner_radius=10)
        self.resumeBtn.place(relx=0.92, rely=0.1, anchor=tkinter.CENTER)

        self.randomPlace = []
        self.answer = num1 + num2
        self.randomPlace.append(self.answer)
        self.showQuestion()
        self.randomAns()
        self.randomBtn()

    def showQuestion(self):
        question = customtkinter.CTkLabel(master=self.addFrm, text=f"{self.num1} + {self.num2} =", font=(self.fFamily, 20, 'bold'), text_color='black')
        question.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    def randomAns(self):
        while len(self.randomPlace) < 4:
            randomNum = random.randint(1, 20)
            if randomNum not in self.randomPlace:
                self.randomPlace.append(randomNum)

    def randomBtn(self):
        random.shuffle(self.randomPlace)
        for idx, value in enumerate(self.randomPlace):
            btn = customtkinter.CTkButton(master=self.addFrm, text=str(value), text_color=self.bgColor, width=100, height=50, font=(self.fFamily, 16, 'bold'))
            btn.place(relx=0.25 + (idx % 2) * 0.5, rely=0.5 + (idx // 2) * 0.2, anchor=tkinter.CENTER)
            if value == self.answer:
                
                btn.configure(command=lambda: print("Correct!"))
            else:
                btn.configure(command=lambda: print("Wrong!"))

# Sample parameters for the class
bgColor = "#ffffff"
fFamily = "Arial"
redColor = "#ff0000"
resumeImg = gameDataAsset.resumeImg

root = tkinter.Tk()
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
Buttons(root, num1, num2, bgColor, fFamily, redColor, resumeImg)
root.mainloop()












# import random


# randomPlace = []
# ranNum = randomPlace.append(random.randint(1, 10))
# def randomBtn():
#     for _ in range(0,3):
#         randomNum = random.randint(1, 10)
#         randomPlace.append(randomNum)
#     return randomPlace
    

# print(type(str(randomBtn()[1])))