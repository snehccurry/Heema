import tkinter as tk
from tkinter import *




root=tk.Tk()


root.geometry("700x400")



b=Label(root,text="Hello world")
b.pack()
def welcome_function(xyz="Nothing"):
	print(xyz)
	Label(root,text="welcome Bosdike").pack()



welcome_button=Button(root, text="Welcome",command=lambda: welcome_function())
welcome_button.pack()


root.config(bg="#679289")





root.mainloop()




