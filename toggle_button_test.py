from Heema import create_window, Button,label_bd
import tkextrafont





root=create_window()

def update():
    if(x.state()=="on"):
        print("settings is on")
    else:
        print("settings is off")


x=SwitchButton(root,on_click=update,toggle_state="on",font=("Segoe UI",40),)

x.pack()


root.mainloop()
