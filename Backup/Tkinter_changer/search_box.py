from Heema import *


root=Tk()
root.geometry("500x300+500+250")
#root.overrideredirect(True)
#title_bar=title_bar(root,text="Abhay")

def update(data):
	#clear the listbox
	my_list.delete(0,END)

	#add toppings to list box

	for item in data:
		my_list.insert(END,item)

#update entry box with listbox clicked

def fillout(e):
	#delet whatever is there in the list box
	my_entry.delete(0,END)
	my_entry.insert(0,my_list.get(ACTIVE))


#create a function ot check entry vs listbox
def check(e):
	#grab what's typed:
	typed= my_entry.get()

	if typed=='':
		data= toppings
	else:
		data=[]
		for item in toppings:
			if typed.lower() in item.lower():
				data.append(item)

	update(data)



label1=Label(root,text="start typing")
label1.pack()

#entry box: 


my_entry=ttk.Entry(root)
my_entry.pack()


my_list=Listbox(root,width=50)
my_list.pack(pady=40)

toppings=["Pepperoni","Peppers","Mushrooms","Cheese","Onions","Ham","Taco"]

#add the toppings to our list
update(toppings)


#create a binding on the listbox onclick

my_list.bind("<<ListboxSelect>>",fillout)	#for list boxes we use doube arrows

my_entry.bind("<KeyRelease>",check)





root.mainloop()