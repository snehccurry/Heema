import mahi
from mahi import *
from mahi import tk 
from mahi import ttk
root=tk.Tk()

root.title("Hello")
mahi.apply_theme() #applies the windowsxp theme, it's what windows 10 actually uses.
root.geometry("400x400")
root.configure(bg=root_bg)

def printer():
	print(f"Button 1 printed succesfully")

def printer2():
	print(f"Button 2 printed succesfully")

a=button(frame_name=root,text_name="Hello world",command=printer)
a.pack()



a2=button(frame_name=root,text_name="Hello world",command=printer)
a2.pack()

#button1=mahi.tk.Button(root,text="Abhay Gaur",="#44444").pack()
root.mainloop()



