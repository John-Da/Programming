from customtkinter import *


app = CTk()
app.geometry("500x400")
app.title("Testing")


fgColor = "#C850C0"
hvColor = "#4158D0"
bdColor = "#FFCC70"
txColor = "#FFCC70"
tetColor = "#0093E9"
ttColor = "#FCAC7E"

# img = ''


label = CTkLabel(master=app, text="Some Text...", font=("Arial", 20), text_color=txColor)

btn = CTkButton(master=app, text="Click Me", corner_radius=12, fg_color=fgColor, hover_color=hvColor, border_color=bdColor, border_width=1)
# btn = CTkButton(master=app, text="Click Me", corner_radius=12, fg_color=fgColor, hover_color=hvColor, border_color=bdColor, border_width=1, image=CTkImage(dark_image=img, light_image=img))

comboBox = CTkComboBox(master=app, values=["option 1", "option 2", "option 3"], fg_color=tetColor, hover=ttColor)

label.place(relx=0.5, rely=0.2, anchor="center")
comboBox.place(relx=0.5, rely=0.4, anchor="center")
btn.place(relx=0.5, rely=0.6, anchor="center")




app.mainloop()




# from customtkinter import *



# app = CTk()
# app.geometry("500x400")


# optionList = [
#     "Option 1",
#     "Option 2",
#     "Option 3"
# ]


# def submit():
#     print(f"Entered value: {entry.get()}")

# def change_handle(value):
#     print(f"Selected Value {value}")


# btn = CTkComboBox(master=app, values=optionList, command=change_handle)

# entry = CTkEntry(master=app, placeholder_text="Type anything...")
# btn = CTkButton(master=app, text="Submit", command=submit)






# btn.place(relx=0.5, rely=0.2, anchor="center")
# entry.pack(anchor="s", expand=True, pady=10)
# btn.pack(anchor="n", expand=True)




# app.mainloop()



# def button_function():
#     app.destroy()
#     w = customtkinter.CTk()
#     w.geometry('1280x720')
#     w.title("Welcome")
#     l1 = customtkinter.CTkLabel(master=w, text="Home Page", font=(fFamily, 60))
#     l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#     w.mainloop()


 # l3 = customtkinter.CTkLabel(master=frame, text="Forget password", font=(fFamily, 12))

    # l3 = customtkinter.CTkLabel(master=frame, text="Creat Account?", font=(fFamily, 12))
    # l3.place(x=30, y=210)


    # loginBtn = customtkinter.CTkButton(master=frame, width=260, height=40, text="Login", font=(fFamily, 20, "bold"), corner_radius=8, command=button_function)
    # loginBtn.place(x=30, y=250)



    # gogIcon = customtkinter.CTkImage(Image.open(gogImg).resize((20, 20), Image.AFFINE))
    # fbIcon = customtkinter.CTkImage(Image.open(fbImg).resize((20, 20), Image.AFFINE))


    # gogBtn = customtkinter.CTkButton(master=frame, image=gogIcon, text="Google", width=120, height=40, corner_radius=8, compound="left", text_color="black", fg_color='white', hover_color="#A4A4A4")
    # gogBtn.place(x=30, y=300)

    # fbBtn = customtkinter.CTkButton(master=frame, image=fbIcon, text="Facebook", width=120, height=40, corner_radius=8, compound="left", text_color="black", fg_color='white', hover_color="#A4A4A4")
    # fbBtn.place(x=171, y=300)



