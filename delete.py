from tkinter import *
import tkinter as tk 
from tkinter import ttk
root=Tk()


root.config(bg="#202020")
style=ttk.Style()

"""
style.theme_settings(themename,{
   "TCombobox": {
       "configure": {"padding": 5},
       "map": {
           "background": [("active", "green2"),
                          ("!disabled", "green4")],
           "fieldbackground": [("!disabled", "green3")],
           "foreground": [("focus", "OliveDrab1"),
                          ("!disabled", "OliveDrab2")]
            },
            }
            })
"""
def hello_world():
    print("Hello world")



windows_themes=['winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative']
root.geometry("400x400")
style.theme_use(themename="xpnative")
print(style.theme_names())

frame1=LabelFrame(root,text="Space",border=0,bg="#202020",fg="#018574",)
frame1.pack(fill='both')
button1=Button(frame1, text="Hello World",border=2, command=hello_world,activebackground="#444444",bg="#202020",fg="#999999", font=('calibri',"20"),bd=0)
button1.pack()


def enter(e):
    print("hovered")
    button1.config(activebackground="#202020",bg="#444444",fg="#ffffff",)#018574

def leave(e):
    print("left")
    button1.config(activebackground="#444444",bg="#202020",fg="#999999")


def clicked(e):
    pass


r= IntVar()
r.set(3)
a=LabelFrame(bg="#202020",bd=0)#fg="#999999"


a.pack()


style.configure("BW.TLabel", foreground="black", background="white")

a1=Radiobutton(a, text="Cool PC at once",bg="#202020",activebackground="#222222",activeforeground="#222222",fg="#999999",font=("Orbitron",14),  variable=r, value=1,command= lambda: clicked(r.get())).pack(side = BOTTOM, pady=1)
Radiobutton(root, text="Cool with sudo powers",bg="#202020",activebackground="#009999",fg="#009999",font=("Orbitron",14),  variable=r, value=2,command= lambda: clicked(r.get())).pack(side = BOTTOM, pady=1)
Radiobutton(root, text="Gain Performance",bg="#202020",activebackground="#009999",fg="#009999",font=("Orbitron",14),  variable=r, value=3,command= lambda: clicked(r.get())).pack(side = BOTTOM, pady=1)
Radiobutton(root, text="Balanced Performance",bg="#202020",activebackground="#009999",fg="#009999",font=("Orbitron",14), variable=r, value=4,command= lambda: clicked(r.get())).pack(side = BOTTOM, pady=1)







button1.bind("<Leave>",leave)
button1.bind("<Enter>",enter)


def enter2(e):
    print("entered frame")
    #a.config(bg="#222222",bd=1)

def leave2(e):
    print("left")
    #a.config(bg="#202020",bd=0)

a.bind("<Leave>",leave2)
a.bind("<Enter>",enter2)




root.mainloop()
