import Heema as h
from Heema import *
from Heema import tk 


#from ctypes import windll

root=tk.Tk()
root.geometry("600x400")
title_bar=title_bar(root,title="Abhay")


def printer():
	print(f"Button 1 printed succesfully")

def printer2():
	print(f"Button 2 printed succesfully")


left_frame=left_frame(frame_name=root)
left_frame.pack(side=LEFT,fill=Y,ipadx=60)

b=left_frame_button(left_frame,text="Classic",command=lambda: apply_theme(root,classic))
b.configure(font=('calibri','11'))
b.pack(fill=X,)


c=left_frame_button(left_frame,text="Dark",command=lambda: apply_theme(root,dark_mode))
c.configure(font=('calibri','11'))
c.pack(fill=X,)

d=left_frame_button(left_frame,text="Super Dark",command=lambda: apply_theme(root,super_dark_mode))
d.configure(font=('calibri','11'))
d.pack(fill=X,)

e=left_frame_button(left_frame,text="Light",command=lambda: apply_theme(root,light_mode))
e.configure(font=('calibri','11'))
e.pack(fill=X,)

f=left_frame_button(left_frame,text="Light Blue",command=lambda: apply_theme(root,light_bluish_mode))
f.configure(font=('calibri','11'))
f.pack(fill=X,)

g=left_frame_button(left_frame,text="Blue Cyan",command=lambda: apply_theme(root,light_blue_cyan_mode))
g.configure(font=('calibri','11'))
g.pack(fill=X,)

h=left_frame_button(left_frame,text="Purple Mode",command=lambda: apply_theme(root,purple_mode))
h.configure(font=('calibri','11'))
h.pack(fill=X,)

i=left_frame_button(left_frame,text="ReddishPurple",command=lambda: apply_theme(root,reddish_purple))
i.configure(font=('calibri','11'))
i.pack(fill=X,)

j=left_frame_button(left_frame,text="ReddishPurple+",command=lambda: apply_theme(root,more_reddish_purple))
j.configure(font=('calibri','11'))
j.pack(fill=X,)

k=left_frame_button(left_frame,text="Purple",command=lambda: apply_theme(root,purple))
k.configure(font=('calibri','11'))
k.pack(fill=X,)

l=left_frame_button(left_frame,text="Reddish",command=lambda: apply_theme(root,reddish))
l.configure(font=('calibri','11'))
l.pack(fill=X,)

m=left_frame_button(left_frame,text="Reddish+",command=lambda: apply_theme(root,full_reddish))
m.configure(font=('calibri','11'))
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
































































































































#title bar for inner code, in case there are bugs encountered.









"""

#this code works fine on windows 10, i didn't try it in any other OS, if you use window 8, 7, ... 
#or you use a distro of linux, you can try it anyway
#this code works fine as a exe made in pyinstaller

tk_title = "tk" # Put here your window title

# root (your app doesn't go in root, it goes in window)
root.title(tk_title) 
root.overrideredirect(True) # turns off title bar, geometry
root.geometry('200x200+75+75') # set new geometry the + 75 + 75 is where it starts on the screen
#root.iconbitmap("your_icon.ico") # to show your own icon 
root.minimized = False # only to know if root is minimized
root.maximized = False # only to know if root is maximized

LGRAY = '#3e4042' # button color effects in the title bar (Hex color)
DGRAY = '#25292e' # window background color               (Hex color)
RGRAY = '#10121f' # title bar color                       (Hex color)

root.config(bg="#25292e")
title_bar = Frame(root, bg=RGRAY, relief='raised', bd=0,highlightthickness=0)


def set_appwindow(mainWindow): # to display the window icon on the taskbar, 
                               # even when using root.overrideredirect(True
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
    root.attributes("-alpha",0) # so you can't see the window when is minimized
    root.minimized = True       


def deminimize(event):

    root.focus() 
    root.attributes("-alpha",1) # so you can see the window when is not minimized
    if root.minimized == True:
        root.minimized = False                              
        

def maximize_me():

    if root.maximized == False: # if the window was not maximized
        root.normal_size = root.geometry()
        expand_button.config(text=" 🗗 ",font=("calibri",14))
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        root.maximized = not root.maximized 
        # now it's maximized
        
    else: # if the window was maximized
        expand_button.config(text=" 🗖 ")
        root.geometry(root.normal_size)
        root.maximized = not root.maximized
        # now it is not maximized

# put a close button on the title bar
close_button = Button(title_bar, text='  ×  ', command=root.destroy,bg=RGRAY,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
expand_button = Button(title_bar, text=' 🗖 ', command=maximize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 14),highlightthickness=0)
minimize_button = Button(title_bar, text=' ─ ',command=minimize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 14),highlightthickness=0)
title_bar_title = Label(title_bar, text=tk_title, bg=RGRAY,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)

# a frame for the main area of the window, this is where the actual app will go
window = Frame(root, bg=DGRAY,highlightthickness=0)


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
    if root.maximized == False:
 
        xwin = root.winfo_x()
        ywin = root.winfo_y()
        startx = event.x_root
        starty = event.y_root

        ywin = ywin - starty
        xwin = xwin - startx

        
        def move_window(event): # runs when window is dragged
            root.config(cursor="fleur")
            root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')


        def release_window(event): # runs when window is released
            root.config(cursor="arrow")
            
            
        title_bar.bind('<B1-Motion>', move_window)
        title_bar.bind('<ButtonRelease-1>', release_window)
        title_bar_title.bind('<B1-Motion>', move_window)
        title_bar_title.bind('<ButtonRelease-1>', release_window)
    else:
        expand_button.config(text=" 🗖 ")
        root.maximized = not root.maximized

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
    xwin = root.winfo_x()
    difference = (event.x_root - xwin) - root.winfo_width()
    
    if root.winfo_width() > 150 : # 150 is the minimum width for the window
        try:
            root.geometry(f"{ root.winfo_width() + difference }x{ root.winfo_height() }")
        except:
            pass
    else:
        if difference > 0: # so the window can't be too small (150x150)
            try:
                root.geometry(f"{ root.winfo_width() + difference }x{ root.winfo_height() }")
            except:
                pass
              
    resizex_widget.config(bg=DGRAY)

resizex_widget.bind("<B1-Motion>",resizex)

# resize the window height
resizey_widget = Frame(window,bg=DGRAY,cursor='sb_v_double_arrow')
resizey_widget.pack(side=BOTTOM,ipadx=2,fill=X)

def resizey(event):
    ywin = root.winfo_y()
    difference = (event.y_root - ywin) - root.winfo_height()

    if root.winfo_height() > 150: # 150 is the minimum height for the window
        try:
            root.geometry(f"{ root.winfo_width()  }x{ root.winfo_height() + difference}")
        except:
            pass
    else:
        if difference > 0: # so the window can't be too small (150x150)
            try:
                root.geometry(f"{ root.winfo_width()  }x{ root.winfo_height() + difference}")
            except:
                pass

    resizex_widget.config(bg=DGRAY)

resizey_widget.bind("<B1-Motion>",resizey)

# some settings
root.bind("<FocusIn>",deminimize) # to view the window by clicking on the window icon on the taskbar
root.after(10, lambda: set_appwindow(root)) # to see the icon on the task bar


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
