# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
import ctypes,platform,win32gui,sys
from BlurWindow.blurWindow import GlobalBlur

DRAG = False

#Colors
FOREGROUND_COLOR = '#FFFFFF'
BACKGROUND_COLOR = '#000000'

BUTTON_BORDER_NOTFOCUSED = '#333333'
BUTTON_BORDER_FOCUSED = '#858585'
BUTTONPRESSED = '#666666'

ENTRY_BORDER_NOTFOCUSED = '#7a7a7a'
ENTRY_BORDER_FOCUSED = '#a7a7a7'
ENTRY_BACKGROUND = '#171717'
ENTRY_BACKGROUNDFOCUSED = '#0e0e0e'
ENTRY_CURSORCOLOR = '#FFFFFF'

DROPDOWN_INACTIVE_BACKGROUND = '#181818'
DROPDOWN_ACTIVE_BACKGROUND = '#3e3d3c'
DROPDOWN_BACKGROUND = '#000000'
DROPDOWN_MENU_BACKGROUND = '#2b2b2b'

def NewButton(parent=None,**kw):
    UWPFONT = Font(family='arial',size=11)
    Border = LabelFrame(parent,
                bd=2, 
                bg=BUTTON_BORDER_NOTFOCUSED, 
                relief=FLAT)
    
    Border.bind("<Enter>", lambda event:[Border.configure(bg=BUTTON_BORDER_FOCUSED)])
    Border.bind("<Leave>", lambda event:[Border.configure(bg=BUTTON_BORDER_NOTFOCUSED)])
    
    b = Button(Border,kw)
    b.configure(borderwidth=0,bg=BUTTON_BORDER_NOTFOCUSED,fg=FOREGROUND_COLOR,font=UWPFONT,
                activebackground=BUTTONPRESSED,activeforeground=FOREGROUND_COLOR)

    if Border.winfo_height() == 1 or Border.winfo_width() == 1:
        Border.configure(height=30,width=90)
    
    Border.bind("<Configure>",lambda event:[b.place(x=Border.winfo_width() /2 - 2,
                                                    y=Border.winfo_height() /2 - 2,
                                                    anchor=CENTER,
                                                    width=Border.winfo_width() -4,
            height=Border.winfo_height() -4)])
    
    return Border,b

def NewEntry(parent=None,**kw):
    UWPFONT = Font(family='arial',size=11)
    Border = LabelFrame(parent,
                bd=2, 
                bg=ENTRY_BORDER_NOTFOCUSED, 
                relief=FLAT)
    
    Border.bind("<Enter>", lambda event:[Border.configure(bg=ENTRY_BORDER_FOCUSED)])
    Border.bind("<Leave>", lambda event:[Border.configure(bg=ENTRY_BORDER_NOTFOCUSED)])
    
    b = Entry(Border,kw)
    b.configure(borderwidth=0,bg=ENTRY_BACKGROUND,fg=FOREGROUND_COLOR,font=UWPFONT,
                insertbackground=ENTRY_CURSORCOLOR,insertwidth=1)
    b.bind("<Enter>", lambda event:[b.configure(bg=ENTRY_BACKGROUNDFOCUSED)])
    b.bind("<Leave>", lambda event:[b.configure(bg=ENTRY_BACKGROUND)])
    
    if Border.winfo_height() == 1 or Border.winfo_width() == 1:
        Border.configure(height=30,width=90)
    
    Border.bind("<Configure>",lambda event:[b.place(x=Border.winfo_width() /2 - 2,
                                                    y=Border.winfo_height() /2 - 2,
                                                    anchor=CENTER,
                                                    width=Border.winfo_width() -4,
            height=Border.winfo_height() -4)])
    
    return Border,b

def CreateDropDownOptions(text,window,UWPFONT,var:StringVar): 
    Border = LabelFrame(window,
                bd=2, 
                bg=DROPDOWN_INACTIVE_BACKGROUND, 
                relief=FLAT)
    Border.configure(height=30,width=90)
    
    Border.bind("<Enter>", lambda event:[Border.configure(bg=BUTTON_BORDER_FOCUSED)])
    Border.bind("<Leave>", lambda event:[Border.configure(bg=DROPDOWN_INACTIVE_BACKGROUND)])
    
    Border.bind("<Configure>",lambda event:[b.place(x=Border.winfo_width() /2 - 2,
                                                    y=Border.winfo_height() /2 - 2,
                                                    anchor=CENTER,
                                                    width=Border.winfo_width() -4,
            height=Border.winfo_height() -4)])
    
    b = Button(Border,text=text,command=lambda:[var.set(text),window.destroy()])
    b.bind("<Enter>", lambda event:[b.configure(bg=DROPDOWN_ACTIVE_BACKGROUND)])
    b.bind("<Leave>", lambda event:[b.configure(bg=DROPDOWN_INACTIVE_BACKGROUND)])
    
    b.configure(borderwidth=0,bg=DROPDOWN_INACTIVE_BACKGROUND,fg=FOREGROUND_COLOR,font=UWPFONT,
                activebackground=BUTTONPRESSED,activeforeground=FOREGROUND_COLOR)
    Border.pack()

def CreateDropDownMenu(var,objs,b:Button):
    root = Tk()
    root.configure(bg=DROPDOWN_MENU_BACKGROUND)
    UWPFONT = Font(family='arial',size=11)
    for i in objs:
        CreateDropDownOptions(i,root,UWPFONT,var)
    rootsize = len(objs) * 20
    geometry = '+%i+%i' % (b.winfo_rootx()-2, b.winfo_rooty()-2 -rootsize /2)
    print(geometry)
    root.geometry(geometry)
    
    root.overrideredirect(1)
    root.mainloop()

def NewDropDown(objs:list,variable:StringVar,**kw):
    UWPFONT = Font(family='arial',size=11)
    Border = LabelFrame(
                bd=2, 
                bg=BUTTON_BORDER_NOTFOCUSED, 
                relief=FLAT)
    
    Border.bind("<Enter>", lambda event:[Border.configure(bg=BUTTON_BORDER_FOCUSED)])
    Border.bind("<Leave>", lambda event:[Border.configure(bg=BUTTON_BORDER_NOTFOCUSED)])
    
    b = Button(Border,kw)
    b.configure(borderwidth=0,bg=BUTTON_BORDER_NOTFOCUSED,fg=FOREGROUND_COLOR,font=UWPFONT,
                activebackground=BUTTONPRESSED,activeforeground=FOREGROUND_COLOR,anchor="w")

    b.configure(command=lambda:[CreateDropDownMenu(var=variable,objs=objs,b=b)])

    if Border.winfo_height() == 1 or Border.winfo_width() == 1:
        Border.configure(height=30,width=90)
        
    b.configure(textvariable=variable)
        
    l = Label(Border,text=u"\uE70D")
    l.configure(bg=BUTTON_BORDER_NOTFOCUSED,fg=FOREGROUND_COLOR)
    
    b.bind("<ButtonPress>", lambda e:l.configure(bg=BUTTONPRESSED))
    b.bind("<ButtonRelease>", lambda e:l.configure(bg=BUTTON_BORDER_NOTFOCUSED))
    
    Border.bind("<Configure>",lambda event:[b.place(x=Border.winfo_width() /2 - 2,
                                                    y=Border.winfo_height() /2 - 2,
                                                    anchor=CENTER,
                                                    width=Border.winfo_width() -4,
                                                    height=Border.winfo_height() -4),
    l.place(y=Border.winfo_height() -25,x= Border.winfo_width() -22)])
    
    return Border,b

def dragging(event,root,HWND):
    global DRAG
    if event.widget is root:
        if DRAG == False:
            GlobalBlur(HWND,Acrylic=False)
        else:
            root.after_cancel(DRAG) 
        DRAG = root.after(200, lambda:stop_drag(HWND))

def stop_drag(HWND):
    global DRAG
    DRAG = False
    GlobalBlur(HWND,Acrylic=True,Dark=True)

def BlurWorkAround(window:Tk,HWND:int):
    GlobalBlur(HWND,Acrylic=True,Dark=True)
    try:release = int(float(platform.release()))
    except:release=False
    
    if release == 10 and IsWin11() == False:
        window.bind('<Configure>', lambda e:dragging(e,window,HWND))

def NewPanel(relx=.4,rely=0,relheight=1,relwidth=1):
    l = Label(bg='#000000')
    l.place(relx=relx,rely=rely,relheight=relheight,relwidth=relwidth)

def NewLabel(size=19,**kw):
    UWPFONT = Font(family='arial',size=size)
    l = Label(font=UWPFONT,bg=BACKGROUND_COLOR,fg=FOREGROUND_COLOR)
    l.configure(kw)
    return l

def IsWin11():
    if sys.getwindowsversion().build > 20000:return True
    else:return False

def TranparentWindow(Window:Tk,color='green'):
    Window.config(bg=color)
    Window.wm_attributes("-transparent", color)

def GetHWNDNew(Window:Tk):
    Window.update()
    hwnd = win32gui.FindWindow(None, Window.title())
    #print(hwnd)
    return hwnd

def GetHWNDTk(Window:Tk):
    Window.focus_force()
    Window.update()
    HWND = ctypes.windll.user32.GetForegroundWindow()
    return HWND 