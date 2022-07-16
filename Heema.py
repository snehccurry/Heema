from tkinter import *
import tkinter as tk
from tkinter import *
from tkinter import ttk



bg="#202020"
root_bg="#202020"


def apply_theme():
	style=ttk.Style()
	style.theme_use(themename="xpnative")


label_border=0
label_bg="#202020"
label_fg="#018574"


def button(frame_name, text_name,command):

	a=Button(frame_name,text=text_name, command=command,border=2,activebackground="#444444",bg="#202020",fg="#999999", font=('calibri',"20"),bd=0)
	def enter(e):
	    #print("hovered")
	    a.config(activebackground="#202020",bg="#444444",fg="#ffffff",)#018574

	def leave(e):
	    #print("left")
	    a.config(activebackground="#444444",bg="#202020",fg="#999999")
	a.bind("<Leave>",leave)
	a.bind("<Enter>",enter)
	return a

button_activebackground="#444444" 
button_bg="#202020" 
button_fg="#999999" 
button_font=('calibri',"20")
button_bd=0


