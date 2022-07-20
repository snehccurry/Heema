import tkinter as tk
from tkinter import *
from tkinter import ttk
import ctypes
from ctypes import windll
from BlurWindow.blurWindow import blur,GlobalBlur

#############################           Theme Names (themenames)


classic='classic'
super_dark_mode='#111111FF' #for super dark mode
dark_mode='#11111199' #for dark mode
light_mode='#30121244' #for light mode
light_blue_cyan_mode='#66999999' #for light blue-cyan theme
light_bluish_mode='#44999999' #for light bluish theme
purple_mode='#44009999' #for purple theme
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





################################################################left frame and buttons
def left_frame(frame_name):
    a=LabelFrame(frame_name,bg="#010101",bd=0)
    a.pack(side=LEFT,fill=Y,ipadx=75,ipady=2,pady=1)
    #print(a.config())
    return a


def left_frame_button(frame_name, text,command):

    a=Button(frame_name,text=text, command=command,border=2,activebackground="#444444",bg="#000000",fg="#999999", font=('calibri',"20"),bd=0,pady=1,padx=1,anchor=W)
    a.pack(fill=X,)
    def enter(e):
        #print("hovered")
        a.config(activebackground="#7e7e7e",bg="#444444",fg="#ffffff",)#018574
        #print(f"a.config is: {a.config()}")
        #7BD5F5
        #205565
        
    def leave(e):
        #print("left")
        a.config(activebackground="#444444",bg="#000000",fg="#999999",anchor=W)
    a.bind("<Leave>",leave)
    a.bind("<Enter>",enter)
    return a



##############################################################Right Frame and buttons


def right_frame(frame_name):
    a=LabelFrame(frame_name,bg="#000000",bd=0,padx=1,pady=1,)
    a.pack(side=RIGHT,fill=Y,ipadx=60)
    #print(a.config())
    return a


def right_frame_button(frame_name, text,command):

    a=Button(frame_name,text=text, command=command,border=2,activebackground="#444444",bg="#000000",fg="#999999", font=('calibri',"20"),bd=0,pady=1,padx=1,anchor=E)
    a.pack(fill=X,)
    def enter(e):
        #print("hovered")
        a.config(activebackground="#7e7e7e",bg="#444444",fg="#ffffff",)#018574
        #print(f"a.config is: {a.config()}")
        #7BD5F5
        #205565
        
    def leave(e):
        #print("left")
        a.config(activebackground="#444444",bg="#000000",fg="#999999",anchor=W)
    a.bind("<Leave>",leave)
    a.bind("<Enter>",enter)
    return a













global_theme="classic"

###############################################Function for themes

def apply_theme(window,theme):
    global global_theme
    style=ttk.Style()
    style.theme_use(themename="xpnative")
    #return window
    if(theme!='classic'):
        root=window
        theme=theme
        global_theme=theme

        mainWindow=window
        HWND = windll.user32.GetParent(mainWindow.winfo_id())
        #root.config(bg='green')
        #root.attributes('-alpha',1)
        #print(root.wm_attributes())
        #root.wm_attributes("-transparent", 'green')
        #root.geometry('500x400')
        root.update()
        HWND = windll.user32.GetParent(mainWindow.winfo_id())

        GlobalBlur(HWND,hexColor=theme,Acrylic=True, Dark=True) #Enable Acrylic
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
        #print(inspect.getargspec(GlobalBlur))
       
        
        global ACRYLIC_ENABLED
        ACRYLIC_ENABLED = True

        global DRAG
        DRAG = False

        def dragging(event):
            global DRAG
            if event.widget is root: #if is event Configure of root (Drag,Resize)
                if DRAG == False:#If Drag is disabled (set by stop_drag)
                    GlobalBlur(HWND,Acrylic=False)
                else:
                    root.after_cancel(DRAG) #cancel task \/ (is dragging)
                DRAG = root.after(200, stop_drag) #execute stop_drag after 200ms

        def stop_drag():
            global DRAG
            DRAG = False
            GlobalBlur(HWND,hexColor=theme,Acrylic=True,Dark=True,) 

        root.bind('<Configure>', dragging)

        #root.mainloop()
    else:
        mainWindow=window
        return


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



######################################title bar
def menu_bar(root):
    r=root
    menu_bar=LabelFrame(r,bg="#000000",fg="#000000",bd=0,highlightthickness=0)
    menu_bar.pack(fill=X,side=TOP)
    return menu_bar

def menu_button(frame_name,text):
    menu_bar=frame_name
    #print(menu_bar)
    l=Button(menu_bar,font=('calibri',"11"),text=text,border=label_bd,bg="#000000",fg="#999999",)
    def enter(e):
        #print("hovered")
        l.config(activebackground="#000000",bg="#202020",fg="#ffffff",)#018574
        #7BD5F5
        #205565
        
    def leave(e):
        #print("left")
        l.config(bg="#000000",fg="#999999",)
    l.bind("<Leave>",leave)
    l.bind("<Enter>",enter)
    l.pack(padx=1,side=LEFT)
    return l

def search_button(frame_name,text,command):
    menu_bar=frame_name
    #print(menu_bar)
    l=Button(menu_bar,font=('calibri',"11"),text=text,border=label_bd,bg="#000000",fg="#ffffff",)
    def enter(e):
        #print("hovered")
        l.config(activebackground="#000000",bg="#202020",fg="#ffffff",command=command)#018574
        #7BD5F5
        #205565
        
    def leave(e):
        #print("left")
        l.config(bg="#000000",fg="#ffffff",)
    l.bind("<Leave>",leave)
    l.bind("<Enter>",enter)
    l.pack(padx=1,side=RIGHT)
    return l

def title_bar(root,text):
    #this code works fine on windows 10, i didn't try it in any other OS, if you use window 8, 7, ... 
    #or you use a distro of linux, you can try it anyway
    #this code works fine as a exe made in pyinstaller

    tk_title = text # Put here your window title

    #root=Tk() # root (your app doesn't go in root, it goes in window)
    root.title(tk_title) 
    root.overrideredirect(True) # turns off title bar, geometry
    #root.geometry('200x200+75+75') # set new geometry the + 75 + 75 is where it starts on the screen
    #root.iconbitmap("your_icon.ico") # to show your own icon 
    root.minimized = False # only to know if root is minimized
    root.maximized = False # only to know if root is maximized

    LGRAY = '#3e4042'   # button color effects in the title bar (Hex color)
    DGRAY = '#202020'   #'#25292e' # window background color               (Hex color)
    RGRAY = '#202020'   #'#10121f'  # title bar color                       (Hex color)

    root.config(bg="#202020")                                                                   #change bg color from here
    title_bar = LabelFrame(root, bg=RGRAY, relief='raised', bd=0,highlightthickness=0)


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
        window.attributes("-alpha",0) # so you can't see the window when is minimized
        window.minimized = True    
        window.bind("<FocusIn>",deminimize) 


    def fake_func(event):
        return None
    def deminimize(event):

        window.focus() 
        window.attributes("-alpha",1) # so you can see the window when is not minimized
        if window.minimized == True:
            window.minimized = False    

        window.bind("<FocusIn>",fake_func)

    def maximize_me():

        if root.maximized == False: # if the window was not maximized
            root.normal_size = "500x80"
            expand_button.config(text=" 🗗 ")
            root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
            root.maximized = not root.maximized 
            # now it's maximized
            
        else: # if the window was maximized
            expand_button.config(text=" 🗖 ")
            root.geometry("800x600")
            root.maximized = not root.maximized
            # now it is not maximized

    # put a close button on the title bar
    close_button = Button(title_bar, text='  ×  ', command=root.destroy,bg=RGRAY,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
    expand_button = Button(title_bar, text=' 🗖 ', command=maximize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
    minimize_button = Button(title_bar, text=' ─ ',command=minimize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
    title_bar_title = Label(title_bar, text=tk_title, bg=RGRAY,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)

    # a frame for the main area of the window, this is where the actual app will go
    #window =mainframe

    # pack the widgets
    
    title_bar.pack(fill=X)
    close_button.pack(side=RIGHT,ipadx=7,ipady=1)
    expand_button.pack(side=RIGHT,ipadx=7,ipady=1)
    minimize_button.pack(side=RIGHT,ipadx=7,ipady=1)

    title_bar_title.pack(side=LEFT, padx=10)
    
    #window.pack() # replace this with your main Canvas/Frame/etc.
    #xwin=None
    #ywin=None
    # bind title bar motion to the move window function

    def changex_on_hovering(event):
        close_button['bg']='red'
        
        
    def returnx_to_normalstate(event):
        close_button['bg']=RGRAY
        

    def change_size_on_hovering(event):
        expand_button['bg']=LGRAY
        
        
    def return_size_on_hovering(event):
        
        expand_button['bg']=RGRAY
        

    def changem_size_on_hovering(event):
        
        minimize_button['bg']=LGRAY
        
        
    def returnm_size_on_hovering(event):
        
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

    window=root
    # resize the window width
    resizex_widget = Frame(window,bg=DGRAY,cursor='sb_h_double_arrow')
    resizex_widget.pack(side=RIGHT,ipadx=2)


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
    root.bind("<FocusOut>",deminimize)
    root.after(1, lambda: set_appwindow(root)) # to see the icon on the task bar



    #YOUR CODE GOES between the lines :)
    # ===================================================================================================





    # Uncomment below to see example of packing a label
    #Label(window,text="Hello :D",bg=DGRAY,fg="#fff").pack(expand=1) # example 





    # ===================================================================================================

    #root.mainloop()


