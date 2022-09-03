

from Heema import *


search_box_window=Tk()
search_box_window.overrideredirect(True)
search_box_window.attributes("-topmost",1)
search_box_window.eval('tk::PlaceWindow . center')
search_box_window.geometry("300x400")
#title_bar=title_bar(search_box_window,text="Search")
search_box_window.config(bg=label_bg)
apply_theme(search_box_window,dark_mode)    






search_and_label_frame=LabelFrame(search_box_window,bg=label_bg,bd=label_bd)
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

search_label_button=button(search_box_window,text="Search 🔎",command=Searchit)
search_label_button.config(font=('Calibri',12),)
search_label_button.pack(side=TOP,pady=4,ipady=5,fill=X)

"""

#entry box: 


search_box=Entry(search_and_label_frame,bd=0,font=('Calibri',12),relief="sunken")
search_box.pack(fill=X,pady=30)




my_list=Listbox(search_box_window,width=50,bd=0,height=7, bg="#202020",fg="#ffffff",font=('Calibri',12),highlightthickness=0,)
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

search_label_button=button(search_box_window,text="Cancel",command=search_box_window.destroy)
search_label_button.config(font=('Calibri',12),)
search_label_button.pack(side=TOP,pady=4,ipady=5,fill=X)

def close_window(e):
    search_box_window.destroy()


#search_box_window.focus()

def check_and_close(e):
    s=my_list.get(ANCHOR)
    if(s==''):
        search_box_window.destroy()
search_box_window.bind('<Escape>',close_window)
search_box_window.bind('<FocusOut>',check_and_close)



#search_box_window.bind('<FocusOut>',close_window)

"""

search_box.bind("<FocusIn>",highlight_box_on)
search_box.bind("<FocusOut>",highlight_box_on)

"""


search_box_window.mainloop()


