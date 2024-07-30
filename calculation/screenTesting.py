from abc import ABC, abstractmethod
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk, ImageFont, ImageDraw
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

# newFont = 'calculation/assets/font/font.ttf'
pixFont = 'calculation/assets/font/newfont.ttf'
welFont = 115





# //////////--------- GAME SCREEN FUNCTION ------------////////////
class Screen:
    def __init__(self, master):
        self.master = master
        self.master.geometry('860x600')
        self.master.title('Basic Math')
        # self.master.configure(bg=BLACK)
        self.customFont = tkFont.Font(family=pixFont, size=welFont, weight='bold')

        self.bg_img = Image.open(bgImg)
        self.bg_photo = ImageTk.PhotoImage(self.bg_img)

        self.bg_label = Label(self.master, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

    def textImage(self):
        image = Image.new('RGB', (860, 600), color=BLACK)


class WelcomePage(Screen):
    def mainScreenLabel(self):
        self.label = tk.Label(self.master, text='Welcome to Basic Math', bg=BLACK, font=self.customFont)
        self.label.place(relx=0.5, rely=0.2, anchor='center')
    

class MenuPage(Screen):
    def __init__(self, master):
        super().__init__(master)


class Buttons:...





def main():
    root = tk.Tk()
    app = Screen(root)
    root.mainloop()


# //////////--------- GUI ------------////////////
if __name__ == "__main__":
    main()
