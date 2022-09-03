import tkinter as tk
from tkinter import *


root=Tk()

root.geometry("600x450")

def print_username():
	print("Welcome Sir, ")

button1=Button(root,text="Hi",command=print_username)

button1.pack(side=BOTTOM)


label=Label(root,text="MY first GUI APP")
label.pack()


root.mainloop()