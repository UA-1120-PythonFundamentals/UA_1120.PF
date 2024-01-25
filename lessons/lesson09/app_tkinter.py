import tkinter
# from tkinter import Button, Frame, LEFT
from tkinter import *
r = tkinter.Tk()

def my_f():
    print("TEXT")

r.title("text")
f = Frame(r)
f.pack()
button = Button(f, text="red", command=my_f)
button.pack(side=LEFT)


my_menu = Menu(r)
r.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="file", menu=file_menu)

file_menu.add_command(label="new")
file_menu.add_command(label="Open..")



help_menu = Menu(my_menu)
my_menu.add_cascade(label="help", menu=help_menu)
help_menu.add_cascade(label="About")
help_menu.add_cascade(label="Exit", command=lambda:quit())


r.mainloop()