from tkinter import *
import tkinter
import customtkinter
from PIL import ImageTk, Image
import ast
# from numba import njit

import gameDataAsset



customtkinter.set_appearance_mode("dark") # light / dark / system
customtkinter.set_default_color_theme("green") # dark-blue, blue, green


app = customtkinter.CTk()
app.geometry("800x600")
app.title("Math Game")

icon = ImageTk.PhotoImage(Image.open(gameDataAsset.gogImg))
app.iconphoto(True, icon)



# =====----- Color / File Path / Font -----=====


fFamily = gameDataAsset.fFamily
redColor = gameDataAsset.redColor
bgColor = gameDataAsset.bgColor
fgColor = gameDataAsset.fgColor


dataSheet = gameDataAsset.dataSheet
bgImg = gameDataAsset.bgImg
gogImg = gameDataAsset.gogImg
fbImg = gameDataAsset.fbImg




# =====----- Screen Loop -----=====

bkImg = ImageTk.PhotoImage(Image.open(bgImg))
l1 = customtkinter.CTkLabel(master=app, image=bkImg)
l1.pack()


def signIn():
# =====----- Sign In Frame -----=====
    signInScreen = customtkinter.CTkFrame(master=l1, width=320, height=380, corner_radius=15)
    signInScreen.place(relx=0.5, rely=0.5, anchor='center')

    l2 = customtkinter.CTkLabel(master=signInScreen, text="Sign In", font=(fFamily, 40, 'bold'), text_color=redColor)
    l2.place(x=104, y=20)



# =====----- UserName Sign In-----=====
    def on_enter(uName):
        userName.delete(0, 'end')
    
    def on_leave(uName):
        if userName.get()=='':
            userName.insert(0, 'Username')


    userName = customtkinter.CTkEntry(master=signInScreen, width=260, height=47)
    userName.bind("<FocusIn>", on_enter)
    userName.bind("<FocusOut>", on_leave)
    userName.insert(0, 'Username')
    userName.place(x=30, y=110)


# =====----- UserPassword Sign In -----=====
    def on_enter(uPassword):
        userPassword.delete(0, 'end')
    
    def on_leave(uPassword):
        if userPassword.get()=='':
            userPassword.insert(0, 'Password')


    userPassword = customtkinter.CTkEntry(master=signInScreen, width=260, height=47)
    userPassword.bind("<FocusIn>", on_enter)
    userPassword.bind("<FocusOut>", on_leave)
    userPassword.insert(0, 'Password')
    userPassword.place(x=30, y=172)
    
    
# =====----- Sigin Check -----=====
    def signInCheck():
        file = open(dataSheet, 'r')
        data = file.read()
        readFile = ast.literal_eval(data)
        file.close()

        key = userName.get()
        value = userPassword.get()

        if key in readFile.keys() and value == readFile[key]:
            app.destroy()


            # import main ------------




        else:
            warningLable = customtkinter.CTkLabel(master=signInScreen, text="Username or Password is wrong!", font=(fFamily, 14, 'bold'), text_color=redColor)
            warningLable.place(x=30, y=82)

        
# =====----- Signin Button -----=====
    
    signinBtn = customtkinter.CTkButton(master=signInScreen, width=260, height=40, text="Sing In", font=(fFamily, 20, "bold"), corner_radius=8, command=signInCheck)
    signinBtn.place(x=30, y=250)

    recomLabel = customtkinter.CTkLabel(master=signInScreen, text="Don't have an account?", text_color=bgColor, font=(fFamily, 12))
    recomLabel.place(x=30, y=292)

    signUpBtn = customtkinter.CTkButton(master=signInScreen, text="Sign Up", text_color=redColor, font=(fFamily, 12), fg_color="transparent", hover=False, command=signUp)
    signUpBtn.place(x=194, y=292)


#//////////////////////////////////#
#//////////////////////////////////#
#//////////////////////////////////#
#//////////////////////////////////#


def signUp():
    # =====----- Sign Up Frame -----=====
    signUpScreen = customtkinter.CTkFrame(master=l1, width=320, height=380, corner_radius=15)
    signUpScreen.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=signUpScreen, text="Sign Up", font=(fFamily, 40, 'bold'), text_color=redColor)
    l2.place(x=104, y=20)


    # =====----- Username Sign Up -----=====
    def on_enter(uName):
        userName.delete(0, 'end')
    
    def on_leave(uName):
        if userName.get()=='':
            userName.insert(0, 'Username')


    userName = customtkinter.CTkEntry(master=signUpScreen, width=260, height=47)
    userName.bind("<FocusIn>", on_enter)
    userName.bind("<FocusOut>", on_leave)
    userName.insert(0, 'Username')
    userName.place(x=30, y=110)


# =====----- UserPassword Sign Up -----=====
    def on_enter(uPassword):
        userPassword.delete(0, 'end')
    
    def on_leave(uPassword):
        if userPassword.get()=='':
            userPassword.insert(0, 'Password')


    userPassword = customtkinter.CTkEntry(master=signUpScreen, width=260, height=47)
    userPassword.bind("<FocusIn>", on_enter)
    userPassword.bind("<FocusOut>", on_leave)
    userPassword.insert(0, 'Password')
    userPassword.place(x=30, y=166)



# =====----- Confirm UserPassword -----======
    def on_enter(uPassword):
        confirmUserPassword.delete(0, 'end')
    
    def on_leave(uPassword):
        if confirmUserPassword.get()=='':
            confirmUserPassword.insert(0, 'Confirm password')


    confirmUserPassword = customtkinter.CTkEntry(master=signUpScreen, width=260, height=47)
    confirmUserPassword.bind("<FocusIn>", on_enter)
    confirmUserPassword.bind("<FocusOut>", on_leave)
    confirmUserPassword.insert(0, 'Confirm password')
    confirmUserPassword.place(x=30, y=224)

    # =====----- Sign Up Checker -----======

    def signUpCheck():
        key = userName.get()
        value = userPassword.get()
        value2 = confirmUserPassword.get()

        if value == value2:
            file = open(dataSheet, 'r+')
            data = file.read()
            readFile = ast.literal_eval(data)

            dict2 = {key:value}
            print(dict2)
            readFile.update(dict2)

            file.truncate(0)
            file.close()

            file = open(dataSheet, 'w')
            w = file.write(str(readFile))

        else:
            warningLable = customtkinter.CTkLabel(master=signUpScreen, text="Username or Password is wrong!", font=(fFamily, 14, 'bold'), text_color=redColor)
            warningLable.place(x=30, y=82)

    signinBtn = customtkinter.CTkButton(master=signUpScreen, width=260, height=40, text="Sing In", font=(fFamily, 20, "bold"), corner_radius=8, command=signUpCheck)
    signinBtn.place(x=30, y=250+30)

    recomLabel = customtkinter.CTkLabel(master=signUpScreen, text="Already have an account?", text_color=bgColor, font=(fFamily, 12))
    recomLabel.place(x=30, y=292+30)

    signUpBtn = customtkinter.CTkButton(master=signUpScreen, text="Sign In", text_color=redColor, font=(fFamily, 12), fg_color="transparent", hover=False, command=signIn)
    signUpBtn.place(x=194, y=292+30)



   



# signIn()
# app.mainloop()