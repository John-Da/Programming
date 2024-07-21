import random
import customtkinter
from PIL import Image, ImageTk
import tkinter
import gameDataAsset

class Buttons:
    def __init__(self, master, bgColor, fFamily, redColor, resumeImg):
        self.master = master
        self.bgColor = bgColor
        self.fFamily = fFamily
        self.redColor = redColor
        self.resumeImg = resumeImg
        self.chances = 3
        self.totalScore = 0

        self.addFrm = customtkinter.CTkFrame(master=self.master, width=720, height=520, corner_radius=15, fg_color=bgColor)
        self.addFrm.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.scoreLabel = customtkinter.CTkLabel(master=self.addFrm, text=f"Score: {self.totalScore}", font=(fFamily, 28, 'bold'), text_color=redColor)
        self.scoreLabel.place(relx=0.15, rely=0.12, anchor=tkinter.CENTER)

        self.chancesLabel = customtkinter.CTkLabel(master=self.addFrm, text=f"Chances: {self.chances}", font=(fFamily, 28, 'bold'), text_color=redColor)
        self.chancesLabel.place(relx=0.74, rely=0.12, anchor=tkinter.CENTER)

        resumeBtnImg = ImageTk.PhotoImage(Image.open(resumeImg).resize((40, 40), Image.AFFINE))
        self.resumeBtn = customtkinter.CTkButton(master=self.addFrm, image=resumeBtnImg, text='', fg_color='transparent', hover=None, width=20, height=20, corner_radius=10)
        self.resumeBtn.place(relx=0.92, rely=0.1, anchor=tkinter.CENTER)
    
        self.generate_question()



    def generate_question(self):
        if self.chances > 0:
            self.num1 = random.randint(1, 10)
            self.num2 = random.randint(1, 10)
            self.randomPlace = []
            self.answer = self.num1 + self.num2
            self.randomPlace.append(self.answer)
            question = customtkinter.CTkLabel(master=self.addFrm, text=f"{self.num1} + {self.num2}", font=(self.fFamily, 20), text_color='black')
            question.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
            self.randomAns()
            self.randomBtn()
        else:
            self.end_game()

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
                btn.configure(command=lambda b=btn: self.correct_answer(b))
            else:
                btn.configure(command=lambda b=btn: self.wrong_answer(b))

    def correct_answer(self, button):
        self.totalScore += 1
        self.scoreLabel.configure(text=f"Score: {self.totalScore}")
        self.clear_buttons()
        self.generate_question()

    def wrong_answer(self, button):
        self.chances -= 1
        self.chancesLabel.configure(text=f"Chances: {self.chances}")
        self.clear_buttons()
        if self.chances > 0:
            self.generate_question()
        else:
            self.end_game()

    def clear_buttons(self):
        for widget in self.addFrm.winfo_children():
            if isinstance(widget, customtkinter.CTkButton) and widget != self.resumeBtn:
                widget.destroy()

    def end_game(self):
        self.clear_buttons()
        endLabel = customtkinter.CTkLabel(master=self.addFrm, text=f"Game Over! Final Score: {self.totalScore}", font=(self.fFamily, 28, 'bold'), text_color=self.redColor)
        endLabel.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Sample parameters for the class
bgColor = "#ffffff"
fFamily = "Arial"
redColor = "#ff0000"
resumeImg = gameDataAsset.resumeImg

root = tkinter.Tk()
# bgImg = gameDataAsset.bgImg
# bkImg = ImageTk.PhotoImage(Image.open(bgImg))
# l1 = customtkinter.CTkLabel(master=root, image=bkImg)
# l1.pack()
Buttons(root, bgColor, fFamily, redColor, resumeImg)
root.mainloop()


# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("green")
# app = customtkinter.CTk()
# app.geometry("800x600")
# app.title("Math Game")


# bgImg = gameDataAsset.bgImg
# bkImg = ImageTk.PhotoImage(Image.open(bgImg))
# l1 = customtkinter.CTkLabel(master=app, image=bkImg)
# l1.pack()
# Buttons(l1, bgColor, fFamily, redColor, resumeImg)
# app.mainloop()
