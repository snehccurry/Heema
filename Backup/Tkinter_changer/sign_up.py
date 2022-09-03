import Heema
from Heema import *
from auth_for_tedsapp import *
root=Tk()
root.geometry("1200x900")
title_bar=title_bar(root,text="Abhay")
menu_bar=menu_bar(root)
zen_mode(root)
def do_nothing():
    pass

def open_search_box():
    #print(global_theme)
    search_box()

menu_button1=menu_button(menu_bar, text="Files")
menu_button2=menu_button(menu_bar, text="Edit")
menu_button3=menu_button(menu_bar, text="Format")
menu_button4=menu_button(menu_bar, text="Views")



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
confirm_password=label(inner_frame,text="Confirm Password: ")

top_frame=LabelFrame(root,bd=0,bg=label_bg)
top_frame.pack(side=TOP)


e1=ttk.Entry(inner_frame,width=35)
e2=ttk.Entry(inner_frame,width=35,show="*")
e3=ttk.Entry(inner_frame,width=35,show="*")


sign_up.grid(row=0,column=0,pady=10)
password.grid(row=1,column=0,padx=10)
confirm_password.grid(row=2,column=0,padx=10)
e1.grid(row=0,column=1,pady=10)
e2.grid(row=1,column=1,pady=10)
e3.grid(row=2,column=1,pady=10)


def sign_up_logic():
    email_id=e1.get()
    password_id=e2.get()
    confirm_password=e3.get()

    if(password_id!=confirm_password):
        a=messagebox(title="Signup",message="different password entered")
    else:
        a=sign_up_now(email_id,password_id)
        if(a=="success"):
            a=messagebox(title="Signup",message="Successfully Signed up, Login with you email and pass")
            

        else:
            a=messagebox(title="Signup",message="Try signing up with a different id/password")





sign_up_btn=label_button(root,text="SignUp", command=sign_up_logic)
sign_up_btn.config(font=('Calibri',12))
sign_up_btn.place(relx=.50,rely=.63)




root.mainloop()