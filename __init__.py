import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
import ctypes
from ctypes import windll
from BlurWindow.blurWindow import blur,GlobalBlur
from PIL import Image, ImageTk
ctypes.windll.shcore.SetProcessDpiAwareness(1)

#############################

bg="#202020"
root_bg="#202020"
label_bd=0
label_bg="#202020"
label_fg="#018574"
symbols=""
#############################           Theme Names (themenames)

"""def page():
    root=Tk()
    
    root.overrideredirect(True)
    #title_bar(root,text="Page 1")
    return root
    #root.mainloop()"""

def do_nothing():
    pass

global screen_width,screen_height

def create_notification(text="Text for windows comes here",button1="Button1",button2="Button2",command1=do_nothing,command2=do_nothing,title="Title comes here...",description="Description comes here..."):
    root=tk.Tk()
    root.overrideredirect(True)
    root.config(bg="#202020")
    title_frame=LabelFrame(root,bd=0,bg=label_bg)
    title_label=Label(title_frame, text=text,bg=label_bg,fg="#ffffff")
    title_label.pack(side=LEFT,fill=X)
    title_frame.pack(fill=X)

    screen_width = int(abs((root.winfo_screenwidth()) *0.20))
    #print(screen_width)

    screen_width_place=int(abs((root.winfo_screenwidth()) *0.79))


    screen_height = int(abs((root.winfo_screenheight()) *0.20))
    #print(screen_height)
    screen_height_place = int(abs((root.winfo_screenheight()) *0.75))

    root.attributes("-topmost",1)


    def close_notification():
        root.destroy()

    close_button=white_label_button(root,text="×",command=close_notification)
    close_button.config(font=('Calibri',18))


    #close_button.pack()
    close_button.place(relx = 0.97, rely =0.05,anchor="center")
    #.place(x=60,y=60)

    root.geometry(f"{screen_width}x{screen_height}+{screen_width_place}+{screen_height_place}")

    main_button_frame=LabelFrame(bg=label_bg,bd=0,highlightthickness=0)
    main_button_frame.pack(side=BOTTOM,fill=X,)
    import time

    button_frame1=LabelFrame(main_button_frame,bg=label_bg,bd=0,highlightthickness=2)
    button_frame2=LabelFrame(main_button_frame,bg=label_bg,bd=0,highlightthickness=2)

    padding=6
    button_frame2.pack(fill=X, side=RIGHT,padx=padding-2,pady=padding-1)
    button_frame1.pack(fill=X, side=RIGHT,padx=padding-2,pady=padding-1)
    
    button1=button(button_frame1,text=button1,command=command1)
    button1.config(font=('calibri',12),highlightthickness=2,bg="#202020")
    button1.pack(fill=X,side=RIGHT,ipadx=0)

    button2=button(button_frame2,text=button2,command=command2)
    button2.config(font=('calibri',12),highlightthickness=2)
    button2.pack(fill=X,side=RIGHT,ipadx=0)

    Title_label=Label(root,text=title,)
    for i in range(screen_width_place*2,screen_width_place,-3):
        #print(screen_width_place)
        root.geometry(f"{screen_width}x{screen_height}+{i}+{screen_height_place}")
        root.update()
    return root


def create_window(text="Text for windows comes here"):
    root=tk.Tk()
    title_bar(root,text=text)
    root.config(bg="#202020")
    Zen_mode(root)
    return root

def create_window_with_no_title_bar(text="Text for windows comes here",bg="#202020"):
    root=tk.Tk()
    root.config(bg=bg)
    root.overrideredirect(True)
    Zen_mode(root)
    return root


def scrollable_frame(window, bg="#202020",y=True,x=False):
    root_frame_for_canvas = LabelFrame(window,bd=label_bd,bg=label_bg)
    canvas = Canvas(root_frame_for_canvas,bg=label_bg,bd=label_bd,highlightthickness=0)
    scrollbar = ttk.Scrollbar(root_frame_for_canvas, orient="vertical", command=canvas.yview)
    scrollable_frame = LabelFrame(canvas,bd=0,highlightthickness=0,bg=label_bg)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    if(y==True):
        canvas.configure(yscrollcommand=scrollbar.set)
    if(x==True):
        canvas.configure(xscrollcommand=scrollbar.set)

    #for i in range(1000):
    #    ttk.Label(scrollable_frame, text=i).pack()


    def scroll_vertical(event):
        """
        Enable vertical scrolling by mouse scroll
        """
        if scrollbar.get() != (0.0, 1.0):
            canvas.yview_scroll(-1 * int(event.delta / 60), "units")


    def scroll_horizontal(event):
        """
        Enable horizontal scrolling by shift + mouse scroll
        """
        if scrollbar.get() != (0.0, 1.0):
            canvas.xview_scroll(-1 * int(event.delta / 60), "units")


    def bound_to_mousewheel(event):
        """
        Bound scrollbar to mouse wheel
        """

        canvas.bind_all('<MouseWheel>', scroll_vertical)
        canvas.bind_all('<Shift-MouseWheel>', scroll_horizontal)


    def unbound_to_mousewheel(event):
        """
        Unbound scrollbar to mouse wheel
        """

        canvas.unbind_all('<MouseWheel>')
        canvas.unbind_all('<Shift-MouseWheel>')
    
    canvas.bind("<Enter>", bound_to_mousewheel)
    canvas.bind("<Leave>", unbound_to_mousewheel)

    root_frame_for_canvas.pack(fill="both",expand=True)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    return scrollable_frame #comment this line and uncomment the upper one if you want to change it. 
    





class create_safe_keypad:
  def __init__(self, frame_name):
    self.frame_name = frame_name
    self.result = tk.StringVar()
    self.full_text=""
    self.bigFont=Font(root=frame_name,family="Helvetica",size=20,weight="bold",underline=0,overstrike=0,)
    l1=Entry(frame_name,bg="#ffffff",bd=0,font=("SegoeUI",18))
    l1.pack(ipadx=50,pady=10,side=TOP)
    main_frame=tk.LabelFrame(frame_name,bg=label_bg,bd=label_bd)
    main_frame.pack()
    buttons_frame=tk.LabelFrame(main_frame,bg=label_bg,bd=0)
    buttons_frame.pack()
    """
    _1=button5(buttons_frame,text="1",command=lambda:update_text(self,text=1))
    _1.pack(ipadx=15,pady=3,padx=3,side=LEFT)
    _2=button5(buttons_frame,text="2",command=lambda:update_text(self,text=2))
    _2.pack(ipadx=15,pady=3,padx=3,side=LEFT)
    _3=button5(buttons_frame,text="3",command=lambda:update_text(self,text=3))
    _3.pack(ipadx=15,pady=3,padx=3,side=LEFT)
    """

    _1=button5(buttons_frame,text="1",command=lambda:update_text(self,text=1))
    _1.grid(row=0,column=0,ipadx=15,pady=3,padx=3)
    _2=button5(buttons_frame,text="2",command=lambda:update_text(self,text=2))
    _2.grid(row=0,column=1,ipadx=15,pady=3,padx=3)
    _3=button5(buttons_frame,text="3",command=lambda:update_text(self,text=3))
    _3.grid(row=0,column=2,ipadx=15,pady=3,padx=3)

    _4=button5(buttons_frame,text="4",command=lambda:update_text(self,text=4))
    _4.grid(row=1,column=0,ipadx=15,pady=3,padx=3)
    _5=button5(buttons_frame,text="5",command=lambda:update_text(self,text=5))
    _5.grid(row=1,column=1,ipadx=15,pady=3,padx=3)
    _6=button5(buttons_frame,text="6",command=lambda:update_text(self,text=6))
    _6.grid(row=1,column=2,ipadx=15,pady=3,padx=3)


    _7=button5(buttons_frame,text="7",command=lambda:update_text(self,text=7))
    _7.grid(row=2,column=0,ipadx=15,pady=3,padx=3)
    _8=button5(buttons_frame,text="8",command=lambda:update_text(self,text=8))
    _8.grid(row=2,column=1,ipadx=15,pady=3,padx=3)
    _9=button5(buttons_frame,text="9",command=lambda:update_text(self,text=9))
    _9.grid(row=2,column=2,ipadx=15,pady=3,padx=3)

    _7=button5(buttons_frame,text="0",command=lambda:update_text(self,text=0))
    _7.grid(row=3,column=0,ipadx=15,pady=3,padx=3,columnspan = 2, sticky = tk.W+tk.E)
    _9=button5(buttons_frame,text=".",command=lambda: update_text(self,text=0))
    _9.grid(row=3,column=2,ipadx=15,pady=3,padx=3,columnspan = 2, sticky = tk.W+tk.E)

    _clear=button5(buttons_frame,text="⌫",command=lambda:update_text(self,text="clear"))
    _clear.config(font=("SegoeUI",16))
    _clear.grid(row=0,column=5,ipadx=15,pady=3,padx=3,rowspan = 4, sticky = tk.N+tk.S)


    def update_text(self,text):
      if(text!="clear"):
        self.full_text=f"{self.full_text}"+f"{text}"
        l1.insert(END,text)
      elif(text=="clear"):
        l1.delete(len(l1.get()) - 1, END)
  def get_text(self):
    return self.full_text
  def get_text_and_clear(self):
    x=self.full_text
    self.full_text=""
    return x


def Zen_mode(root):
    screen_width = int(abs((root.winfo_screenwidth()) *0.85))
    #print(screen_width)

    screen_width_place=int(abs((root.winfo_screenwidth()) *0.07))


    screen_height = int(abs((root.winfo_screenheight()) *0.85))
    #print(screen_height)
    screen_height_place = int(abs((root.winfo_screenheight()) *0.07))



    root.geometry(f"{screen_width}x{screen_height}+{screen_width_place}+{screen_height_place}")


def zen_mode(root):
    #root.wm_attributes("-topmost",1)
    screen_width = int(abs((root.winfo_screenwidth()) *0.7))
    #print(screen_width)

    screen_width_place=int(abs((root.winfo_screenwidth()) *0.15))


    screen_height = int(abs((root.winfo_screenheight()) *0.7))
    #print(screen_height)
    screen_height_place = int(abs((root.winfo_screenheight()) *0.15))



    root.geometry(f"{screen_width}x{screen_height}+{screen_width_place}+{screen_height_place}")




def page_geometry(root):
    root.wm_attributes("-topmost",1)
    screen_width = int(abs((root.winfo_screenwidth()) *0.7))
    #print(screen_width)

    screen_width_place=int(abs((root.winfo_screenwidth()) *0.15))


    screen_height = int(abs((root.winfo_screenheight()) *0.7))
    #print(screen_height)
    screen_height_place = int(abs((root.winfo_screenheight()) *0.15))



    root.geometry(f"{screen_width}x{screen_height}+{screen_width_place}+{screen_height_place}")


def messagebox_geometry(root):
    root.wm_attributes("-topmost",1)
    screen_width = int(abs((root.winfo_screenwidth()) *0.2))
    #print(screen_width)

    screen_width_place=int(abs((root.winfo_screenwidth()) *0.4))


    screen_height = int(abs((root.winfo_screenheight()) *0.25))
    #print(screen_height)
    screen_height_place = int(abs((root.winfo_screenheight()) *0.4))



    root.geometry(f"{screen_width}x{screen_height}+{screen_width_place}+{screen_height_place}")


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


def label(frame_name,text,bg=label_bg):
    a=Label(frame_name,bd=label_bd,text=text,bg=bg,fg="#ffffff")
    return a


back_buttons=['','','','']
back_buttons_all=""
keyboard_buttons="⌨⌫"


def back_button(frame_name,text="",command=do_nothing):
    l=Button(frame_name,font=('SegoeUI',"26"),text=text,border=label_bd,bg=label_bg,fg="#ffffff",bd=0,command=command)
    def enter(e):
        #print("hovered")
        l.config(text="",activebackground="#202020",bg="#202020")#018574
        #7BD5F5
        #205565
        
    def leave(e):
        #print("left")
        l.config(text="",bg="#202020",fg="#ffffff")
    l.bind("<Leave>",leave)
    l.bind("<Enter>",enter)
    return l
def forward_button(frame_name,text="",command=do_nothing):
    l=Button(frame_name,font=('SegoeUI',"26"),text=text,border=label_bd,bg=label_bg,fg="#ffffff",bd=0,command=command)
    def enter(e):
        #print("hovered")
        l.config(text="",activebackground="#202020",bg="#202020")#018574
        #7BD5F5
        #205565
        
    def leave(e):
        #print("left")
        l.config(text="",bg="#202020",fg="#ffffff")
    l.bind("<Leave>",leave)
    l.bind("<Enter>",enter)
    return l

def label_button(frame_name,text,command=do_nothing):
    l=Button(frame_name,font=('calibri',"11"),text=text,border=label_bd,bg=label_bg,fg=label_fg,bd=0,command=command)
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
def white_label_button(frame_name,text,command=do_nothing):
    l=Button(frame_name,font=('calibri',"11"),text=text,border=label_bd,bg=label_bg,fg="#999999",command=command)
    def enter(e):
        #print("hovered")
        l.config(activebackground="#202020",bg="#202020",fg="#ffffff",)#018574
        #7BD5F5
        #205565
        
    def leave(e):
        #print("left")
        l.config(bg="#202020",fg="#999999")
    l.bind("<Leave>",leave)
    l.bind("<Enter>",enter)
    return l

def orange_label_button(frame_name,text,command=do_nothing):
    l=Button(frame_name,font=('calibri',"11"),text=text,border=label_bd,bg=label_bg,fg="#CC4329",command=command)
    def enter(e):
        #print("hovered")
        l.config(activebackground="#000000",bg="#000000",fg="#ffffff",)#018574
        #7BD5F5
        #205565
        
    def leave(e):
        #print("left")
        l.config(bg="#000000",fg="#CC4329")
    l.bind("<Leave>",leave)
    l.bind("<Enter>",enter)
    return l


def button(frame_name, text,command):

    a=Button(frame_name,text=text, command=command,border=0,activebackground="#444444",bg="#202020",fg="#999999", font=('calibri',"20"),bd=0)
    def enter(e):
        #print("hovered")
        a.config(bd=0,activebackground="#7e7e7e",bg="#444444",fg="#ffffff",)#018574
        #7BD5F5
        #205565
        
    def leave(e):
        #print("left")
        a.config(bd=0,activebackground="#444444",bg="#202020",fg="#999999")
    a.bind("<Leave>",leave)
    a.bind("<Enter>",enter)
    return a

def button1(frame_name, text,command):

    a=Button(frame_name,text=text, command=command,border=0,activebackground="#444444",bg="#202020",fg="#999999", font=('calibri',"20"),bd=0)
    def enter(e):
        #print("hovered")
        a.config(bd=0,activebackground="#7e7e7e",bg="#444444",fg="#ffffff",)#018574
        #7BD5F5
        #205565
        
    def leave(e):
        #print("left")
        a.config(bd=0,activebackground="#444444",bg="#202020",fg="#999999")
    a.bind("<Leave>",leave)
    a.bind("<Enter>",enter)
    return a

def button2(frame_name, text,command):

    a=Button(frame_name,text=text, command=command,border=0,activebackground="#444444",bg="#2f2f2f",fg="#ffffff", font=('calibri',"20"),bd=0)
    def enter(e):
        #print("hovered")
        a.config(bd=0,activebackground="#7e7e7e",bg="#EBEBEB",fg="#000000",)#018574
        #7BD5F5
        #205565
        
    def leave(e):
        #print("left")
        a.config(bd=0,activebackground="#444444",bg="#2f2f2f",fg="#ffffff")
    a.bind("<Leave>",leave)
    a.bind("<Enter>",enter)
    return a




def button3(frame_name, text,command):

    a=Button(frame_name,text=text, command=command,border=0,activebackground="#444444",bg="#2f2f2f",fg="#ffffff", font=('calibri',"20"),bd=0)
    def enter(e):
        #print("hovered")
        a.config(bd=0,activebackground="#CC4329",bg="#EBEBEB",fg="#000000",)#018574
        #7BD5F5
        #205565
        
    def leave(e):
        #print("left")
        a.config(bd=0,activebackground="#444444",bg="#2f2f2f",fg="#ffffff")
    a.bind("<Leave>",leave)
    a.bind("<Enter>",enter)
    return a


def button4(frame_name, text,command):

    a=Button(frame_name,text=text, command=command,border=0,activebackground="#444444",bg="#2f2f2f",fg="#ffffff", font=('calibri',"20"),bd=0)
    def enter(e):
        #print("hovered")
        a.config(bd=0,activebackground="#7e7e7e",bg="#3f3f3f",fg="#ffffff",)#018574
        #7BD5F5
        #205565
        
    def leave(e):
        #print("left")
        a.config(bd=0,activebackground="#444444",bg="#2f2f2f",fg="#ffffff")
    a.bind("<Leave>",leave)
    a.bind("<Enter>",enter)
    return a

def button5(frame_name, text,command):

    a=Button(frame_name,text=text, command=command,border=0,activebackground="#444444",bg="#2f2f2f",fg="#ffffff", font=('calibri',"20"),bd=0)
    def enter(e):
        #print("hovered")
        a.config(bd=0,activebackground="#EBEBEB",bg="#CC4329",fg="#ffffff",)#018574
        #7BD5F5
        #2055651
        
    def leave(e):
        #print("left")
        a.config(bd=0,activebackground="#444444",bg="#2f2f2f",fg="#ffffff")
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
    menu_bar.pack(fill=X,side=TOP )
    return menu_bar

def menu_button(frame_name,text,command=do_nothing):
    menu_bar=frame_name
    #print(menu_bar)
    l=Button(menu_bar,font=('calibri',"11"),text=text,border=label_bd,bg="#000000",fg="#999999",command=command)
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

        #window.focus() 
        window.attributes("-alpha",1) # so you can see the window when is not minimized
        if window.minimized == True:
            window.minimized = False    

        window.bind("<FocusIn>",fake_func)
         

                

    def maximize_me():

        if root.maximized == False: # if the window was not maximized
            root.normal_size = root.geometry()
            expand_button.config(text=" 🗗 ")
            root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
            root.maximized = not root.maximized 
            # now it's maximized
            
        else: # if the window was maximized
            expand_button.config(text=" 🗖 ")
            Zen_mode(root)
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


def search_box():
    root=Tk()
    root.overrideredirect(True)
    root.attributes("-topmost",1)
    root.eval('tk::PlaceWindow . center')
    root.geometry("300x400")
    #title_bar=title_bar(root,text="Search")
    root.config(bg=label_bg)
    apply_theme(root,dark_mode)    






    search_and_label_frame=LabelFrame(root,bg=label_bg,bd=label_bd)
    search_and_label_frame.pack(side=TOP,fill=X)




    search_label=Label(search_and_label_frame, text="Search 🔎" ,bg=label_bg,bd=label_bd,fg="#999999",font=('Calibri',12))
    search_label.pack(fill=X)


    def update(data):
        #clear the listbox
        my_list.delete(0,END)
        #add everything to list box

        for item in data:
            my_list.insert(END,item)

    #update entry box with listbox clicked

    def fillout(e):
        #delet whatever is there in the list box
        search_box.delete(0,END)
        print(my_list.get(ANCHOR))
        search_box.insert(0,my_list.get(ANCHOR))
        a=my_list.get(ANCHOR)
        return a


    #create a function ot check entry vs listbox
    def check(e):
        #grab what's typed:
        typed= search_box.get()

        if typed=='':
            data= everything
        else:
            data=[]
            for item in everything:
                if typed.lower() in item.lower():
                    data.append(item)
        update(data)

    """def Searchit():
        print(search_box.get())

        pass

    search_label_button=button(root,text="Search 🔎",command=Searchit)
    search_label_button.config(font=('Calibri',12),)
    search_label_button.pack(side=TOP,pady=4,ipady=5,fill=X)

    """

    #entry box: 


    search_box=Entry(search_and_label_frame,bd=0,font=('Calibri',12),relief="sunken")
    search_box.pack(fill=X,pady=30)




    my_list=Listbox(root,width=50,bd=0,height=7, bg="#202020",fg="#ffffff",font=('Calibri',12),highlightthickness=0,)
    my_list.pack(fill=BOTH, padx=5,pady=30)

    everything=["Music","Videos","Internet","Account","Settings","Valut","Logout"]




    #add the everything to our list
    update(everything)


    #create a binding on the listbox onclick

    my_list.bind("<<ListboxSelect>>",fillout)   #for list boxes we use doube arrows
    search_box.bind("<KeyRelease>",check)







    def printer(e):
        print("Hello")

    search_box.focus()
    #search_box.bind("<FocusOut>",printer)

    search_label_button=button(root,text="Cancel",command=root.destroy)
    search_label_button.config(font=('Calibri',12),)
    search_label_button.pack(side=TOP,pady=4,ipady=5,fill=X)

    def close_window(e):
        root.destroy()


    #root.focus()

    def check_and_close(e):
        s=my_list.get(ANCHOR)
        if(s==''):
            root.destroy()
    root.bind('<Escape>',close_window)
    root.bind('<FocusOut>',check_and_close)
    root.bind('<FocusOut>',check_and_close)
    search_box.after(1,lambda: search_box.focus_force())

    #root.bind('<FocusOut>',close_window)

    """

    search_box.bind("<FocusIn>",highlight_box_on)
    search_box.bind("<FocusOut>",highlight_box_on)

    """

    root.mainloop()


def dock_geometry(root,side):
    root.wm_attributes("-topmost",1)
    screen_width = int(abs((root.winfo_screenwidth()) *0.7))
    #print(screen_width)

    screen_width_place=int(abs((root.winfo_screenwidth()) *0.15))


    screen_height = int(abs((root.winfo_screenheight()) *0.2))
    #print(screen_height)
    screen_height_place = int(abs((root.winfo_screenheight()) *0.02))



    root.geometry(f"{screen_width}x{screen_height}+{screen_width_place}+{screen_height_place}")

def create_dock(bg=label_bg,side="bottom"):
    root=tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost",1)

    dock_geometry(root,side=side)
    apply_theme(root,dark_mode)
    root.config(bg=bg)
    def close_window(e):
        root.destroy()
    root.bind('<Escape>',close_window)
    root.focus_force()
    #root.mainloop()
    return root




def menu_page(text,bg=label_bg):

    root=tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost",1)

    page_title_frame=LabelFrame(root,highlightthickness=0,bg=bg,bd=0)
    page_title_frame.pack(fill=X,)
    title=label(page_title_frame,text=text,bg=bg)
    title.config(font=('Calibri',11))
    title.pack(side=LEFT,ipadx=5,ipady=3)
    page_geometry(root)

    apply_theme(root,dark_mode)
    root.config(bg=bg)
    def close_window(e):
        root.destroy()
    root.bind('<Escape>',close_window)
    root.bind('<FocusOut>',close_window)
    root.focus_force()
    #root.mainloop()
    return root


def messagebox(title,message="Your Message Here...",text="ok"):
    root=Tk()
    root.overrideredirect(True)
    root.attributes("-topmost",1)
    page_title_frame=LabelFrame(root,highlightthickness=0,bg=label_bg,bd=0)
    page_title_frame.pack(fill=X,)
    title_label=label(page_title_frame,text=title)
    title_label.config(font=('Calibri',16))
    title_label.pack(side=LEFT,ipadx=5,ipady=3)
    messagebox_geometry(root)
    root.config(bg=label_bg)
    apply_theme(root,dark_mode)
    def close_window(e):
        root.destroy()
    root.bind('<Escape>',close_window)
    root.bind('<FocusOut>',close_window)
    root.focus_force()
    message=Label(root,text=message,bg=label_bg,bd=label_bd,fg=label_fg,)
    message.pack(fill=BOTH,pady=50)
    b=button(root,text="    ok    ",command=lambda: root.destroy())
    b.config(font=('Calibri',14))
    b.pack(fill=X,side=BOTTOM,pady=10)
    #root.mainloop()
    return root


######################for the image engine


def image(frame_name,path,bg=label_bg):
    image1 = Image.open(path)
    test = ImageTk.PhotoImage(image1,master = frame_name)

    label1 = Label(frame_name,image=test,bg=label_bg,bd=label_bd)
    label1.image = test

    return label1
def create_image(frame_name,path,size,bg=label_bg):
    image1 = Image.open(path)
    
    resize_image = image1.resize((size,size))
    test = ImageTk.PhotoImage(resize_image,master = frame_name)
    label1 = Label(frame_name,image=test,bd=0,bg=label_bg)

    label1.image = test

    return label1


def resized_image(frame_name,path,size,bg=label_bg):
    image1 = Image.open(path)
    
    resize_image = image1.resize((size,size))
    test = ImageTk.PhotoImage(resize_image,master = frame_name)
    label1 = Label(frame_name,image=test,bd=0,bg=label_bg)

    label1.image = test

    return label1

def zen_image(frame_name,path):
    image1 = Image.open(path)
    root=frame_name
    screen_width = int(abs((root.winfo_screenwidth()) *0.93))
    screen_height=int(abs((root.winfo_screenheight()))*0.96)
    print(screen_height,screen_width)
    resize_image = image1.resize((screen_width,screen_height))
    test = ImageTk.PhotoImage(resize_image,master = frame_name)
    label1 = Label(frame_name,image=test,bd=0)

    label1.image = test

    return label1





########################## image engine programs





def navigate_to(main_frame ,welcome_page):
    main_frame.forget()
    welcome_page.pack(fill=BOTH,expand=True)






