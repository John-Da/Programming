from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import messagebox
# import ast





# /====------ Screen ------=====/
screen = Tk()
screen.geometry('800x600')
screen.title('Math Game')



# /====------ Color / Font / File Path ------=====/
fFamily = 'Century Gothic'
ligthFont = 'Microsoft YaHei UI Light'


redColor = '#ff4f5a'
bgColor = '#A9A9A9'
fgColor = 'black'
tranColor = '#FFFFFF'


dataSheet = "ownExplore/customTTk/userData.txt"


bgImg = "ownExplore/customTTk/assets/pattern.png"
gogImg = "ownExplore/customTTk/assets/Google__G__Logo.svg.webp"
fbImg = "ownExplore/customTTk/assets/124010.png"


background = PhotoImage(file=bgImg)






# /====------ Function ------=====/
def signIn():
    backgroundImage = Canvas(screen, width=800, height=400)
    backgroundImage.pack(fill='both', expand=True)
    backgroundImage.create_image(0,0, image = background, anchor='center')

    signInScreen = Frame(screen, width=360, height=410, bg=bgColor)
    signInScreen.place(x=230, y=90)

    signInLable = Label(signInScreen, text="Sign In", fg=redColor, bg=bgColor)
    signInLable.config(font=(ligthFont, 38, 'bold'))
    signInLable.place(x=140, y=26)







signIn()
screen.mainloop()