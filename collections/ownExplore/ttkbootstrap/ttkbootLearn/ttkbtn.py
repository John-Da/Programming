from tkinter import *
import ttkbootstrap as tb



# Root
root = tb.Window(themename='superhero')
root.title('TTK Bootstrap')
root.iconbitmap('images/icon.ico')
root.geometry('600x400')



def checker():
    if var1.get() == 1:
        my_label.config(text='Checked')
    else:
        my_label.config(text='Unchecked')



my_label = Label(text="Click button", font=('Helvetica', 28))
my_label.pack(pady=(40, 10))

var1 = IntVar()
my_check = tb.Checkbutton(bootstyle='primary', text='Check Me Out', variable=var1, onvalue=1, offvalue=0, command=checker)
my_check.pack(pady=10)


var2 = IntVar()
my_check2 = tb.Checkbutton(bootstyle='danger, toolbutton', text='Tool Button', variable=var2, onvalue=1, offvalue=0, command=checker)
my_check2.pack(pady=10)


var3 = IntVar()
my_check3 = tb.Checkbutton(bootstyle='danger, toolbutton, outline', text='Outlined ToolButton', variable=var3, onvalue=1, offvalue=0, command=checker)
my_check3.pack(pady=10)


var4 = IntVar()
my_check4 = tb.Checkbutton(bootstyle='success, round-toggle', text='Round Toggle', variable=var4, onvalue=1, offvalue=0, command=checker)
my_check4.pack(pady=10)


var5 = IntVar()
my_check5 = tb.Checkbutton(bootstyle='warning, square-toggle', text='Round Toggle', variable=var5, onvalue=1, offvalue=0, command=checker)
my_check5.pack(pady=10)

root.mainloop()