from Heema import *
from PIL import ImageTk, Image
from cards2 import *

root=Tk()


super_frame=LabelFrame(root)


card_frame1=LabelFrame(super_frame,bg="blue", bd=label_bd)
card_frame2=LabelFrame(super_frame,bg=label_bg, bd=label_bd)
card_frame3=LabelFrame(super_frame,bg=label_bg, bd=label_bd)

a=card(card_frame1,"Account","Your account realted settings.",image="images/logo.png",x=90,y=90)
a.pack(fill=X,)


b=card(card_frame1,"Settings","All the settings are here.",image="images/logo.png",x=90,y=90)
b.pack(fill=X,)

c=card(card_frame1,"Themes","Customize themes for the window.",image="images/logo.png",x=90,y=90)
c.pack(fill=X,)

d=card(card_frame2,"Work","Your work places in Space.",image="images/logo.png",x=90,y=90)
d.pack(fill=X,)


e=card(card_frame2,"Utilities","Utilities related settings.",image="images/logo.png",x=90,y=90)
e.pack(fill=X,)


f=card(card_frame2,"Documents","View all your documents.",image="images/logo.png",x=90,y=90)
f.pack(fill=X,)

g=card(card_frame3,"Facebook","Facebook images and posts.",image="images/logo.png",x=90,y=90)
g.pack(fill=X,)

card_frame1.pack(fill=X,anchor=W)
card_frame2.pack(fill=X,anchor=W)
card_frame3.pack(fill=X,anchor=W)


super_frame.pack(fill=BOTH,expand=True,anchor=W)

root.mainloop()

"""
        self.label.pack()
        self.description.pack(padx=4)
self.description.pack(padx=4)"""