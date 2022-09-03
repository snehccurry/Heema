from cmath import log
from Heema import *
from auth_for_tedsapp import *
root=Tk()
root.geometry("1200x900")
title_bar=title_bar(root,text="Abhay")
menu_bar=menu_bar(root)
zen_mode(root)

def do_nothing():
    pass

menu_button1=menu_button(menu_bar, text="Files",command=do_nothing)
menu_button2=menu_button(menu_bar, text="Edit",command=do_nothing)
menu_button3=menu_button(menu_bar, text="Format",command=do_nothing)
menu_button4=menu_button(menu_bar, text="Views",command=do_nothing)


def open_search_box():
    #print(global_theme)
    search_box()
    #print(f"Opened search box \U0001F50D ")


search_button=search_button(menu_bar, text="Search \t \U0001F50D", command=open_search_box)


left_frame=left_frame(frame_name=root)


b=left_frame_button(left_frame,text="Classic",command=lambda: apply_theme(root,classic))
b.configure(font=('calibri','12'))



c=left_frame_button(left_frame,text="Dark",command=lambda: apply_theme(root,dark_mode))
c.configure(font=('calibri','12'))


d=left_frame_button(left_frame,text="Super Dark",command=lambda: apply_theme(root,super_dark_mode))
d.configure(font=('calibri','12'))


e=left_frame_button(left_frame,text="Light",command=lambda: apply_theme(root,light_mode))
e.configure(font=('calibri','12'))


f=left_frame_button(left_frame,text="Light Blue",command=lambda: apply_theme(root,light_bluish_mode))
f.configure(font=('calibri','12'))






centre_frame=LabelFrame(root,bd=0,bg=label_bg)
centre_frame.place(relx=.5, rely=.5,anchor= CENTER,)

inner_frame=LabelFrame(centre_frame,bd=0,bg=label_bg)
inner_frame.pack(padx=50,pady=50)

sign_up=label(inner_frame,text="ID: ")
password=label(inner_frame,text="Pass: ")

top_frame=LabelFrame(root,bd=0,bg=label_bg)
top_frame.pack(side=TOP)


e1=ttk.Entry(inner_frame,width=35)
e2=ttk.Entry(inner_frame,width=35,show="*")


sign_up.grid(row=0,column=0,pady=10)
password.grid(row=1,column=0,padx=10)
e1.grid(row=0,column=1,pady=10)
e2.grid(row=1,column=1,padx=10)

def login_logic():
    email=e1.get()
    password=e2.get()
    a=login(email,password)
    if(a=="success"):
        a=messagebox("Login","Successfully logged in")
    else:
        a=messagebox(title="Login",message="Login Failed, please check your email/password",)


login_btn=label_button(root,text=" Login ",command=login_logic)
login_btn.config(font=('Calibri',12))
login_btn.place(relx=.50,rely=.6)



root.mainloop()