import tkinter as tk
from Heema import *
from PIL import ImageTk, Image
# Your class
class card():
    
    '''This class sets the baseline characteristics 
    for the widgets, including font, font size, and colors
    '''
    # Attributes
    varFont = "Calibri"
    fontSize = 14
    varFG = label_fg
    varBG = label_bg
    # Constructor
    def __init__(self, frame_name, title="your title here",description="your description here",image="images\\image1.png",x=100,y=70):
        label_frame_for_card=LabelFrame(frame_name,bg=label_bg,bd=2,fg=label_fg,width=100,height=50)
        logo_image = Image.open(image)
        resize_image = logo_image.resize((x,y))
        logo_app_image = ImageTk.PhotoImage(resize_image)

        logo=tk.Label(label_frame_for_card,image=logo_app_image)
        logo.image=logo_app_image
        logo.pack(side=LEFT)
        
        self.label_frame_for_card  = label_frame_for_card
        self.title = title
        sub_frame=LabelFrame(label_frame_for_card,bg=label_bg,bd=label_bd,fg=label_fg)
        self.label = tk.Label(
            sub_frame, 
            text = title, 
            fg = "#ffffff", 
            bg = self.varBG,
            justify="left", 
            font = (self.varFont, self.fontSize),
            wraplength=150,
            anchor=W
            )
        
        self.description=tk.Label(sub_frame,text=description, justify="left",wraplength=150,fg="#999999",bg=label_bg,font=(self.varFont,int(self.fontSize*0.70)))
        #self.label.pack()
        #self.description.pack(padx=4)
        
        
        sub_frame.pack(side=LEFT,anchor=W)
        label_frame_for_card.pack(fill=BOTH,expand=True,side=LEFT)
    # Allows you to grid as you would normally
    # Can subsitute pack() here or have both class methods
    def grid(self,row,column, **kwargs,):
        self.label.grid(kwargs,row=row,column=column)
        self.description.grid(kwargs,row=row,column=column)

    def pack(self, **kwargs):
        self.label.pack(kwargs,anchor=W,padx=3)
        self.description.pack(anchor=W,padx=4)
        #self.logo.pack(kwargs,side=LEFT)

    def config(self,**kwargs):
        self.label.config(kwargs)

    def paras():
        print("frame_name, title, title,image=images\\image1.png,x=100,y=70):")
    def cardprint():
        paras()
    def parameters():
        paras()
