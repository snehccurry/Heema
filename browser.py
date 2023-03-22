import sys
import ctypes
import platform
import tkinter as tk
from cefpython3 import cefpython as cef
import time
# platforms
WINDOWS = 'Windows'
browser_settings = {
    "javascript": True,
}

settings = { 
}
'''
if MAC:
settings["external_message_pump"] = True
'''
cef.Initialize(settings=settings)
global app_url
app_url="https://www.google.com"

class BrowserFrame(tk.Frame):
    global app_url
    def __init__(self,master=None, **kw):
        super().__init__(master,**kw)
        self.browser = None
        self.bind('<Configure>', self.on_configure)

    def get_window_handle(self):
        '''
        if MAC:
            from AppKit import NSApp
            import objc
            return objc.pyobjc_id(NSApp.windows()[-1].contentView())
        '''
        if self.winfo_id() > 0:
            return self.winfo_id()
        else:
            raise Exception('Could not obtain window handle!')

    def on_configure(self, event):
        #global cef_winfo
        global cef_winfo
        if self.browser is None:
            # create the browser and embed it in current frame
            rect = [0, 0, self.winfo_width(), self.winfo_height()]
            cef_winfo = cef.WindowInfo()
            win_id = self.get_window_handle()
            cef_winfo.SetAsChild(win_id, rect)
            #print("win info is: "+ str(cef_winfo))
            self.browser = cef.CreateBrowserSync(cef_winfo, url=app_url)

            # start the browser handling loop
            self.cef_loop()

        # resize the browser
        if WINDOWS:
            ctypes.windll.user32.SetWindowPos(
                self.browser.GetWindowHandle(), 0,
                0, 0, event.width, event.height, 0x0002)
        '''
        elif LINUX:
            self.browser.SetBounds(0, 0, event.width, event.height)
        '''

    def cef_loop(self):
        cef.MessageLoopWork()
        self.after(10, self.cef_loop)













