import Heema as h
from Heema import *
from Heema import tk 
from pages import *

window1=tk.Tk()
title_bar=title_bar(window1,text="Abhay")
Zen_mode(window1)


main_frame=LabelFrame(window1,bd=0,bg=label_bg)
main_frame.pack(fill=BOTH,expand=True)


menu_bar=menu_bar(main_frame)
#menu_bar.pack(fill=X,side=TOP)
menu_button1=menu_button(menu_bar, text="Files",command=files_page)
menu_button2=menu_button(menu_bar, text="Edit",command=edit_page)
menu_button3=menu_button(menu_bar, text="Format",command=format_page)
menu_button4=menu_button(menu_bar, text="Views",command=views_page)
menu_button5=menu_button(menu_bar, text="Settings",command=settings_page)
menu_button6=menu_button(menu_bar, text="Run",command=run_page)
menu_button7=menu_button(menu_bar, text="Help",command=help_page)



def Welcome_page():
    Welcome_page=scrollable_frame(window1)
    

    b1=button(Welcome_page,text="Hello Work",command=do_nothing)
    b1.pack(anchor="center")
    b2=button1(Welcome_page,text="Hello Work",command=do_nothing)
    b2.pack()
    b3=button2(Welcome_page,text="Hello Work",command=do_nothing)
    b3.pack()
    b4=button3(Welcome_page,text="Hello Work",command=do_nothing)
    b4.pack()
    b5=button4(Welcome_page,text="Hello Work",command=do_nothing)
    b5.pack()
    b6=button5(Welcome_page,text="Hello Work",command=do_nothing)
    b6.pack()

    image1=image(Welcome_page,path="C:\\Users\\The AR Station\\Pictures\\Spidey_shocked.jpg")
    image1.pack()
    for i in range(100):
        label(Welcome_page,text=f"Scrollable frame test: {i}").pack(pady=10)


    label1=label_button(Welcome_page,text="Open Settings",command=do_nothing)
    label1.pack()

    return Welcome_page



def open_search_box():
    #print(global_theme)
    search_box()
    #print(f"Opened search box \U0001F50D ")


search_button=search_button(menu_bar, text="Search \t \U0001F50D", command=open_search_box)




def printer():
    print(f"Button 1 printed succesfully")

def printer2():
    print(f"Button 2 printed succesfully")


left_frame=left_frame(frame_name=main_frame)


b=left_frame_button(left_frame,text="Classic",command=lambda: apply_theme(window1,classic))
b.configure(font=('calibri','12'))



c=left_frame_button(left_frame,text="Dark",command=lambda: apply_theme(window1,dark_mode))
c.configure(font=('calibri','12'))


d=left_frame_button(left_frame,text="Super Dark",command=lambda: apply_theme(window1,super_dark_mode))
d.configure(font=('calibri','12'))


e=left_frame_button(left_frame,text="Light",command=lambda: apply_theme(window1,light_mode))
e.configure(font=('calibri','12'))


f=left_frame_button(left_frame,text="Light Blue",command=lambda: apply_theme(window1,light_bluish_mode))
f.configure(font=('calibri','12'))


g=left_frame_button(left_frame,text="Blue Cyan",command=lambda: apply_theme(window1,light_blue_cyan_mode))
g.configure(font=('calibri','12'))


h=left_frame_button(left_frame,text="Purple Mode",command=lambda: apply_theme(window1,purple_mode))
h.configure(font=('calibri','12'))


i=left_frame_button(left_frame,text="ReddishPurple",command=lambda: apply_theme(window1,reddish_purple))
i.configure(font=('calibri','12'))


j=left_frame_button(left_frame,text="ReddishPurple+",command=lambda: apply_theme(window1,more_reddish_purple))
j.configure(font=('calibri','12'))


k=left_frame_button(left_frame,text="Purple",command=lambda: apply_theme(window1,purple))
k.configure(font=('calibri','12'))


l=left_frame_button(left_frame,text="Reddish",command=lambda: apply_theme(window1,reddish))
l.configure(font=('calibri','12'))


m=left_frame_button(left_frame,text="Reddish+",command=lambda: apply_theme(window1,full_reddish))
m.configure(font=('calibri','12'))


#main_frame.title("Hello")

#main_frame.geometry("400x400")


a=button2(frame_name=main_frame,text="Hello world",command=printer)
a.pack(side=TOP, ipadx=50)

def navigator():
    main_frame.pack_forget()
    Welcome_page()




a2=button(frame_name=main_frame,text="Hello world",command=navigator)
a2.pack(side=TOP, ipadx=50)




l1=label_button(frame_name=main_frame,text="My Microsoft account")
l1.pack(side=TOP)



#some serious fun is going on here, XDD funny as fuck lol
#s1=ttk.Button(main_frame,text="OLD FASHINOED WINDOWS BUTTON LOL").pack()
#button1=Heema.tk.Button(main_frame,text="Abhay Gaur",="#44444").pack()


labelframe1=LabelFrame(main_frame,bg=bg ,text="Buttons for next",bd=label_bd)
labelframe1.pack()


"""
from PIL import ImageTk, Image
my_img1=ImageTk.PhotoImage(Image.open("Screenshots/Smallview.png"))

image_label=Label(image=my_img1)
image_label.pack()

"""






if global_theme=='light_mode':
    image_label.forget()






##################          ROOT MAINLOOP()
main_frame.mainloop()


























































#main_frame.wm_attributes("-transparentcolor", '#F0F0F0')
#print(main_frame.attributes())
#print(main_frame.wm_attributes())




#apply_theme(main_frame,super_dark_mode) #applies the windowsxp theme, it's what windows 10 actually uses.
apply_theme(window1,classic)
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



































































































































#title bar for inner code, in case there are bugs encountered.









"""

#this code works fine on windows 10, i didn't try it in any other OS, if you use window 8, 7, ... 
#or you use a distro of linux, you can try it anyway
#this code works fine as a exe made in pyinstaller

tk_title = "tk" # Put here your window title

# main_frame (your app doesn't go in main_frame, it goes in window)
main_frame.title(tk_title) 
main_frame.overrideredirect(True) # turns off title bar, geometry
main_frame.geometry('200x200+75+75') # set new geometry the + 75 + 75 is where it starts on the screen
#main_frame.iconbitmap("your_icon.ico") # to show your own icon 
main_frame.minimized = False # only to know if main_frame is minimized
main_frame.maximized = False # only to know if main_frame is maximized

LGRAY = '#3e4042' # button color effects in the title bar (Hex color)
DGRAY = '#25292e' # window background color               (Hex color)
RGRAY = '#10121f' # title bar color                       (Hex color)

main_frame.config(bg="#25292e")
title_bar = Frame(main_frame, bg=RGRAY, relief='raised', bd=0,highlightthickness=0)


def set_appwindow(mainWindow): # to display the window icon on the taskbar, 
                               # even when using main_frame.overrideredirect(True
    # Some WindowsOS styles, required for task bar integration
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    # Magic
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
   
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())
    

def minimize_me():
    main_frame.attributes("-alpha",0) # so you can't see the window when is minimized
    main_frame.minimized = True       


def deminimize(event):

    main_frame.focus() 
    main_frame.attributes("-alpha",1) # so you can see the window when is not minimized
    if main_frame.minimized == True:
        main_frame.minimized = False                              
        

def maximize_me():

    if main_frame.maximized == False: # if the window was not maximized
        main_frame.normal_size = main_frame.geometry()
        expand_button.config(text=" 🗗 ",font=("calibri",14))
        main_frame.geometry(f"{main_frame.winfo_screenwidth()}x{main_frame.winfo_screenheight()}+0+0")
        main_frame.maximized = not main_frame.maximized 
        # now it's maximized
        
    else: # if the window was maximized
        expand_button.config(text=" 🗖 ")
        main_frame.geometry(main_frame.normal_size)
        main_frame.maximized = not main_frame.maximized
        # now it is not maximized

# put a close button on the title bar
close_button = Button(title_bar, text='  ×  ', command=main_frame.destroy,bg=RGRAY,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
expand_button = Button(title_bar, text=' 🗖 ', command=maximize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 14),highlightthickness=0)
minimize_button = Button(title_bar, text=' ─ ',command=minimize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 14),highlightthickness=0)
title_bar_title = Label(title_bar, text=tk_title, bg=RGRAY,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)

# a frame for the main area of the window, this is where the actual app will go
window = Frame(main_frame, bg=DGRAY,highlightthickness=0)


def changex_on_hovering(event):
    global close_button
    close_button['bg']='red'
    
    
def returnx_to_normalstate(event):
    global close_button
    close_button['bg']=RGRAY
    

def change_size_on_hovering(event):
    global expand_button
    expand_button['bg']=LGRAY
    
    
def return_size_on_hovering(event):
    global expand_button
    expand_button['bg']=RGRAY
    

def changem_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=LGRAY
    
    
def returnm_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=RGRAY
    

def get_pos(event): # this is executed when the title bar is clicked to move the window
    if main_frame.maximized == False:
 
        xwin = main_frame.winfo_x()
        ywin = main_frame.winfo_y()
        startx = event.x_main_frame
        starty = event.y_main_frame

        ywin = ywin - starty
        xwin = xwin - startx

        
        def move_window(event): # runs when window is dragged
            main_frame.config(cursor="fleur")
            main_frame.geometry(f'+{event.x_main_frame + xwin}+{event.y_main_frame + ywin}')


        def release_window(event): # runs when window is released
            main_frame.config(cursor="arrow")
            
            
        title_bar.bind('<B1-Motion>', move_window)
        title_bar.bind('<ButtonRelease-1>', release_window)
        title_bar_title.bind('<B1-Motion>', move_window)
        title_bar_title.bind('<ButtonRelease-1>', release_window)
    else:
        expand_button.config(text=" 🗖 ")
        main_frame.maximized = not main_frame.maximized

title_bar.bind('<Button-1>', get_pos) # so you can drag the window from the title bar
title_bar_title.bind('<Button-1>', get_pos) # so you can drag the window from the title 

# button effects in the title bar when hovering over buttons
close_button.bind('<Enter>',changex_on_hovering)
close_button.bind('<Leave>',returnx_to_normalstate)
expand_button.bind('<Enter>', change_size_on_hovering)
expand_button.bind('<Leave>', return_size_on_hovering)
minimize_button.bind('<Enter>', changem_size_on_hovering)
minimize_button.bind('<Leave>', returnm_size_on_hovering)

# resize the window width
resizex_widget = Frame(window,bg=DGRAY,cursor='sb_h_double_arrow')
resizex_widget.pack(side=RIGHT,ipadx=2,fill=Y)


def resizex(event):
    xwin = main_frame.winfo_x()
    difference = (event.x_main_frame - xwin) - main_frame.winfo_width()
    
    if main_frame.winfo_width() > 150 : # 150 is the minimum width for the window
        try:
            main_frame.geometry(f"{ main_frame.winfo_width() + difference }x{ main_frame.winfo_height() }")
        except:
            pass
    else:
        if difference > 0: # so the window can't be too small (150x150)
            try:
                main_frame.geometry(f"{ main_frame.winfo_width() + difference }x{ main_frame.winfo_height() }")
            except:
                pass
              
    resizex_widget.config(bg=DGRAY)

resizex_widget.bind("<B1-Motion>",resizex)

# resize the window height
resizey_widget = Frame(window,bg=DGRAY,cursor='sb_v_double_arrow')
resizey_widget.pack(side=BOTTOM,ipadx=2,fill=X)

def resizey(event):
    ywin = main_frame.winfo_y()
    difference = (event.y_main_frame - ywin) - main_frame.winfo_height()

    if main_frame.winfo_height() > 150: # 150 is the minimum height for the window
        try:
            main_frame.geometry(f"{ main_frame.winfo_width()  }x{ main_frame.winfo_height() + difference}")
        except:
            pass
    else:
        if difference > 0: # so the window can't be too small (150x150)
            try:
                main_frame.geometry(f"{ main_frame.winfo_width()  }x{ main_frame.winfo_height() + difference}")
            except:
                pass

    resizex_widget.config(bg=DGRAY)

resizey_widget.bind("<B1-Motion>",resizey)

# some settings
main_frame.bind("<FocusIn>",deminimize) # to view the window by clicking on the window icon on the taskbar
main_frame.after(10, lambda: set_appwindow(main_frame)) # to see the icon on the task bar


# pack the widgets
title_bar.pack(fill=X)
close_button.pack(side=RIGHT,ipadx=7,ipady=1)
expand_button.pack(side=RIGHT,ipadx=7,ipady=1)
minimize_button.pack(side=RIGHT,ipadx=7,ipady=1)
title_bar_title.pack(side=LEFT, padx=10)
window.pack(expand=1, fill=BOTH) # replace this with your main Canvas/Frame/etc.
#xwin=None
#ywin=None
# bind title bar motion to the move window function
#YOUR CODE GOES between the lines :)
# ===================================================================================================





# Uncomment below to see example of packing a label
#Label(window,text="Hello :D",bg=DGRAY,fg="#fff").pack(expand=1) # example 





# ===================================================================================================








"""
