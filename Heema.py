import tkinter as tk
from tkinter import *
from tkinter import ttk
from titlebar import *


#############################			Theme Names (themenames)


classic='classic'
super_dark_mode='#111111FF' #for super dark mode
dark_mode='#11111199' #for dark mode
light_mode='#30121244' #for light mode
light_blue_cyan_theme='#66999999' #for light blue-cyan theme
light_bluish_theme='#44999999' #for light bluish theme
purple_theme='#44009999' #for purple theme
reddish_purple='#30121244' #for reddish purple
more_reddish_purple='#30121277' #for more redish purple
purple='#99004444' #for purple
reddish='#99000044' #for reddish
full_reddish='#99000099' #for full reddish



#############################

bg="#202020"
root_bg="#202020"





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









##############################Themes

#111111FF #for super dark mode
#11111199 #for dark mode
#30121244 #for light mode
#66999999 #for light blue-cyan theme
#44999999 #for light bluish theme
#44009999 #for purple theme
#30121244 #for reddish purple
#30121277 #for more redish purple
#99004444 #for purple
#99000044 #for reddish
#99000044 #for dark redish
#99000099 #for full redish


