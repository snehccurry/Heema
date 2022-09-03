from Heema import *
import Heema
window1=Tk()




screen_width = int(abs((window1.winfo_screenwidth())))
screen_height = int(abs((window1.winfo_screenheight()) *0.90))


root_frame=LabelFrame(window1,width=300,height=300,bg=label_bg, bd=label_bd)
root_frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
canvas=Canvas(root_frame,bg=label_bg,width=screen_width,height=screen_height,scrollregion=(0,0,500,500))
hbar=Scrollbar(root_frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(root_frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width=screen_width,height=screen_height)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)



window1.mainloop()



#screen_width = int(abs((root.winfo_screenwidth()) *0.85))
#screen_height = int(abs((root.winfo_screenheight()) *0.85))