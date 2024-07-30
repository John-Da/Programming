from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import customtkinter as ctk
# import os


# //////////--------- ASSETS ------------////////////
bgImg = 'calculation/assets/img/bgg.png'

BLACK = '#000000'
RED = '#D10000'
GRAY = '#BEBEBE'
WHITE = '#FFFFFF'
PURPLE = '#823BF6'
ORANGE = '#FF5C00'
GREEN = '#228851'
BLUE = '#2690CC'
YELLOW = '#ABA406'
LIGHT_GREEN = '#00FD84'
DARK_RED = '#A24B4B'


REDHOVER = '#FF7D33'

# newFont = 'calculation/assets/font/font.ttf'
pixFont = "Helvetica"
welFont = 115
strtFont = 58
menuFont = 74
optionFont = 40

CURSOR = 'hand2'





# //////////--------- GAME SCREEN FUNCTION ------------////////////
class Screen:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1980x960')
        self.master.title('Basic Math')
        # self.master.configure(bg=BLACK)

        self.bg_img = Image.open(bgImg)
        self.bg_photo = ImageTk.PhotoImage(self.bg_img)

        self.bg_label = Label(self.master, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)
        

class WelcomePage(Screen):
    def __init__(self, master):
        super().__init__(master)
        self.mainScreenFrame()

    def mainScreenFrame(self):
        self.welTitle = ctk.CTkFont(family=pixFont, size=welFont, weight='bold')
        self.welcome = Label(self.master, text='Welcome to Basic Math', font=self.welTitle, bg=BLACK)
        self.welcome.place(relx=0.5, rely=0.2, anchor='center')

        self.startTxt = ctk.CTkFont(family=pixFont, size=strtFont, weight='bold')
        self.startBtn = ctk.CTkButton(self.master, text="START", fg_color=ORANGE, bg_color=BLACK, font=self.startTxt, width=250, height=105, corner_radius=15, hover_color=REDHOVER, cursor=CURSOR, command=self.showMenu)
        self.startBtn.place(relx=0.5, rely=0.6, anchor='center')
        

    def showMenu(self):
        self.welcome.destroy()
        self.startBtn.destroy()
        MenuPage(self.master)


class UserName(Screen):
    def __init__(self, master):
        super().__init__(master)
        self.getUserName()
    
    def getUserName(self):
        ...
        

class MenuPage(Screen):
    def __init__(self, master):
        super().__init__(master)
        self.menuLabel()

    def menuLabel(self):
        self.menuTitle = ctk.CTkFont(family=pixFont, size=menuFont, weight='bold')
        self.menu_label = ctk.CTkLabel(self.master, text='What do you like to play?', font=self.menuTitle, fg_color=WHITE)
        self.menu_label.place(relx=0.5, rely=0.2, anchor='center')



class Buttons:...





def main():
    root = tk.Tk()
    app = WelcomePage(root)
    root.mainloop()


# //////////--------- GUI ------------////////////
if __name__ == "__main__":
    main()
