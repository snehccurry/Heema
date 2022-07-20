import Heema as h
from Heema import *
from Heema import tk 


#from ctypes import windll

root=tk.Tk()
root.geometry("800x500")
title_bar=title_bar(root,title="Abhay")


def printer():
	print(f"Button 1 printed succesfully")

def printer2():
	print(f"Button 2 printed succesfully")


left_frame=left_frame(frame_name=root)
left_frame.pack(side=LEFT,fill=Y,ipadx=60)

b=left_frame_button(left_frame,text="Classic",command=lambda: apply_theme(root,classic))
b.configure(font=('calibri','12'))
b.pack(fill=X,)


c=left_frame_button(left_frame,text="Dark",command=lambda: apply_theme(root,dark_mode))
c.configure(font=('calibri','12'))
c.pack(fill=X,)

d=left_frame_button(left_frame,text="Super Dark",command=lambda: apply_theme(root,super_dark_mode))
d.configure(font=('calibri','12'))
d.pack(fill=X,)

e=left_frame_button(left_frame,text="Light",command=lambda: apply_theme(root,light_mode))
e.configure(font=('calibri','12'))
e.pack(fill=X,)

f=left_frame_button(left_frame,text="Light Blue",command=lambda: apply_theme(root,light_bluish_mode))
f.configure(font=('calibri','12'))
f.pack(fill=X,)

g=left_frame_button(left_frame,text="Blue Cyan",command=lambda: apply_theme(root,light_blue_cyan_mode))
g.configure(font=('calibri','12'))
g.pack(fill=X,)

h=left_frame_button(left_frame,text="Purple Mode",command=lambda: apply_theme(root,purple_mode))
h.configure(font=('calibri','12'))
h.pack(fill=X,)

i=left_frame_button(left_frame,text="ReddishPurple",command=lambda: apply_theme(root,reddish_purple))
i.configure(font=('calibri','12'))
i.pack(fill=X,)

j=left_frame_button(left_frame,text="ReddishPurple+",command=lambda: apply_theme(root,more_reddish_purple))
j.configure(font=('calibri','12'))
j.pack(fill=X,)

k=left_frame_button(left_frame,text="Purple",command=lambda: apply_theme(root,purple))
k.configure(font=('calibri','12'))
k.pack(fill=X,)

l=left_frame_button(left_frame,text="Reddish",command=lambda: apply_theme(root,reddish))
l.configure(font=('calibri','12'))
l.pack(fill=X,)

m=left_frame_button(left_frame,text="Reddish+",command=lambda: apply_theme(root,full_reddish))
m.configure(font=('calibri','12'))
m.pack(fill=X,)

#root.title("Hello")

#root.geometry("400x400")


a=button(frame_name=root,text="Hello world",command=printer)
a.pack(side=TOP)



a2=button(frame_name=root,text="Works",command=printer2)
a2.pack(side=TOP)


l1=label_button(frame_name=root,text="My Microsoft account")
l1.pack(side=TOP)



#some serious fun is going on here, XDD funny as fuck lol
#s1=ttk.Button(root,text="OLD FASHINOED WINDOWS BUTTON LOL").pack()
#button1=Heema.tk.Button(root,text="Abhay Gaur",="#44444").pack()


labelframe1=LabelFrame(root,bg=bg ,text="Buttons for next",bd=label_bd)
labelframe1.pack()
#button1=Button(labelframe1,text="button").pack()
#blurrer(root)

#root.wm_attributes("-transparentcolor", '#F0F0F0')



#print(root.attributes())
#print(root.wm_attributes())




#apply_theme(root,super_dark_mode) #applies the windowsxp theme, it's what windows 10 actually uses.
#apply_theme(root,classic)
"""
super_dark_mode='#111111FF' #for super dark mode
dark_mode='#11111199' #for dark mode
light_mode='#30121244' #for light mode
light_blue_cyan_theme='#66999999' #for light blue-cyan theme
light_bluish theme='#44999999' #for light bluish theme
purple_theme='#44009999' #for purple theme
reddish_purple='#30121244' #for reddish purple
more_reddish_purple='#30121277' #for more redish purple
purple='#99004444' #for purple
reddish='#99000044' #for reddish
full_reddish'#99000099' #for full reddish
"""


root.mainloop()
















