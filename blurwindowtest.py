#https://github.com/sourcechord/FluentWPF/issues/42#issuecomment-873615119 idea
from tkinter import *
import ctypes
from ctypes import windll
from BlurWindow.blurWindow import blur,GlobalBlur
import inspect
#root = Tk()


def blurrer(window):
    #return window
    root=window
    mainWindow=window
    HWND = windll.user32.GetParent(mainWindow.winfo_id())
    #root.config(bg='green')
    #root.attributes('-alpha',1)
    print(root.wm_attributes())
    #root.wm_attributes("-transparent", 'green')
    #root.geometry('500x400')
    root.update()
    HWND = windll.user32.GetParent(mainWindow.winfo_id())

    GlobalBlur(HWND,hexColor='#11111199',Acrylic=True, Dark=True) #Enable Acrylic
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
    print(inspect.getargspec(GlobalBlur))
   
    
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
            DRAG = root.after(100, stop_drag) #execute stop_drag after 200ms

    def stop_drag():
        global DRAG
        DRAG = False
        GlobalBlur(HWND,hexColor='#11111199',Acrylic=True,Dark=True,) 

    root.bind('<Configure>', dragging)

    #root.mainloop()
