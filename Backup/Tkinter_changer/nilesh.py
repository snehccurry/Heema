from Heema import *


root= Tk()


title_bar(root,"Counter")


count=0

def on_plus():
	global count
	count+=1
	label1.config(text=count)
	


def on_sub():
	global count
	count-=1
	label1.config(text=count)





label_frame=LabelFrame(root,bg=label_bg, bd=label_bd, highlightbackground=None)


b1=button(label_frame,text="+",command=on_plus)
b1.grid(row=0,column=0,ipadx=50)



label1=label(label_frame,text=count)

label1.grid(row=0,column=1,ipadx=50)


b2=button(label_frame,text="-",command=on_sub)
b2.grid(row=0,column=2,ipadx=50)


label_frame.pack(fill=BOTH)



root.geometry("800x650")

#apply_theme(root,dark_mode)

root.mainloop()