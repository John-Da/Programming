import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random


root = tk.Tk()
root.title('App')
# root.eval('tk::PlaceWindow . center')
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('500x800+' + str(x) + '+' + str(y))

reLogo1 = '/Users/yendahwa/Desktop/MyStuff/MyWorks/myGitHub/Programming/ownExplore/ttkbootstrap/ttk/assets/RRecipe_logo.png'
reLogo2 = '/Users/yendahwa/Desktop/MyStuff/MyWorks/myGitHub/Programming/ownExplore/ttkbootstrap/ttk/assets/RRecipe_logo_bottom.png'

dataBase = '/Users/yendahwa/Desktop/MyStuff/MyWorks/myGitHub/Programming/ownExplore/ttkbootstrap/ttk/data/recipes.db'

bgColor = '#3d6466'
darkerCol = '#28393a'
badeeCol = '#badee2'



def fetch_db():
    connection = sqlite3.connect(dataBase)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()

    idx = random.randint(0, len(all_tables)-1)
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()

    connection.close()
    return table_records, table_name



def pre_process(table_name, table_records):
    title = table_name[:-6]
    title = "".join([char if char.islower() else " " + char for char in title])

    ingredients = []

    for i in table_records:
        name = i[1]
        qty = i[2]
        unit = i[3]
        ingredients.append(qty + " " + unit + " of " + name)
    
    return title, ingredients
    


def load_frame1():
    frame1.tkraise()
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file=reLogo1)
    logo_widget = tk.Label(frame1, image=logo_img, bg=bgColor)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(
        frame1, text="Random recipe?",
        bg= bgColor,
        fg="white",
        font=('TkMenuFont', 18)
    ).pack()

    tk.Button(
        frame1, 
        text='SHUFFLE',
        font=("TkHeadingFont", 20),
        bg=darkerCol,
        fg='white',
        cursor='hand2',
        activebackground=badeeCol,
        activeforeground='black',
        command=lambda:load_frame2()
    ).pack(pady=20)


def load_frame2():
    frame2.tkraise()
    table_name, table_records = fetch_db()
    title, ingredients = pre_process(table_name, table_records)

    logo_img = ImageTk.PhotoImage(file=reLogo2)
    logo_widget = tk.Label(frame2, image=logo_img, bg=bgColor)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Label(
        frame2, 
        text=title,
        bg= bgColor,
        fg="white",
        font=('TkHeadingFont', 20)
    ).pack(pady=25)

    for i in ingredients:
        tk.Label(
            frame2, 
            text=i,
            bg= bgColor,
            fg="white",
            font=('TkHeadingFont', 12)
    ).pack(pady=25)
        
    tk.Button(
        frame1, 
        text='BACK',
        font=("TkHeadingFont", 18),
        bg=darkerCol,
        fg='white',
        cursor='hand2',
        activebackground=badeeCol,
        activeforeground='black',
        command=lambda:load_frame1()
    ).pack(pady=20)




frame1 = tk.Frame(root, width=500, height=800, bg=bgColor)
frame2 = tk.Frame(root, bg=bgColor)
frame1.grid(row=0, column=0)
# frame2.grid(row=0, column=0)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)
    


load_frame1()



root.mainloop()