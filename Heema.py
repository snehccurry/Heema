import tkinter as tk
from tkinter import *
from tkinter import ttk
from titlebar import *


bg="#202020"
root_bg="#202020"



def apply_theme():
	style=ttk.Style()
	style.theme_use(themename="xpnative")

def apply_transparency(root):
	root.attributes('-alpha',0.96)
label_bd=0
label_bg="#202020"
label_fg="#018574"



def label_button(frame_name,text):
	l=Button(frame_name,font=('calibri',"11"),text=text,border=label_bd,bg=label_bg,fg=label_fg)
	def enter(e):
	    #print("hovered")
	    l.config(activebackground="#202020",bg="#202020",fg="#ffffff",)#018574
	    #7BD5F5
	    #205565
	    
	def leave(e):
	    #print("left")
	    l.config(bg="#202020",fg="#009999")
	l.bind("<Leave>",leave)
	l.bind("<Enter>",enter)
	return l

def button(frame_name, text,command):

	a=Button(frame_name,text=text, command=command,border=2,activebackground="#444444",bg="#202020",fg="#999999", font=('calibri',"20"),bd=0)
	def enter(e):
	    #print("hovered")
	    a.config(activebackground="#7e7e7e",bg="#444444",fg="#ffffff",)#018574
	    #7BD5F5
	    #205565
	    
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






def left_frame(frame_name):
	a=LabelFrame(frame_name,bg="#000000",bd=0,padx=1,pady=1)
	return a


def left_frame_button(frame_name, text,command):

	a=Button(frame_name,text=text, command=command,border=2,activebackground="#444444",bg="#000000",fg="#999999", font=('calibri',"20"),bd=0,pady=1,padx=1)
	def enter(e):
	    #print("hovered")
	    a.config(activebackground="#7e7e7e",bg="#444444",fg="#ffffff",)#018574
	    #7BD5F5
	    #205565
	    
	def leave(e):
	    #print("left")
	    a.config(activebackground="#444444",bg="#000000",fg="#999999")
	a.bind("<Leave>",leave)
	a.bind("<Enter>",enter)
	return a
