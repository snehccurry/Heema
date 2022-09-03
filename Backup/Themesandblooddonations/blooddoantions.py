import time
import pandas as pd

from tkinter import *
import tkinter as tk 


root=tk.Tk()


root.configure(bg="#000000")
v=Scrollbar(root, orient='vertical')
v.pack(side=RIGHT, fill='y')

input_box = Text(root, height = 40,
                width = 150,
                bg = "light blue",yscrollcommand=v.set,)
input_box.config(state= DISABLED)
input_box.pack(fill='both')

def recipient_finder(donor_input):
	donor=donor_input
	if(donor=="O-"):
		recipients=["AB+","AB-","A+","A-","B+","B-","O+","O-"]
	elif(donor=="O+"):
		recipients=["AB+","A+","B+","O+"]
	elif(donor=="B-"):
		recipients=["AB+","AB-","B+","B-"]
	elif(donor=="B+"):
		recipients=["AB+","B+"]
	elif(donor=="A-"):
		recipients=["AB+","AB-","A+","A-"]
	elif(donor=="A+"):
		recipients=["AB+","A+"]
	elif(donor=="AB-"):
		recipients=["AB+","AB-"]
	elif(donor=="AB+"):
		recipients="AB+"
	else:
		recipients="Invalid Input, restart the program"
	#print(f"{donor} can donate to : {recipients}")
	input_box.config(state= NORMAL)
	input_box.insert(END,f"{donor} can donate to : {recipients} \n")
	input_box.config(state= DISABLED)

#global recipient_input
#recipient_input="A+"

def donor_finder(recipient_input):
	recipient=recipient_input

	if(recipient=="AB+"):
		donors=["O-","O+","B-","B+","A-","A+","AB-","AB+"]
	elif(recipient=="AB-"):
		donors=["O-","B-","A-","AB-"]
	elif(recipient=="A+"):
		donors=["O-","O+","A-","A+"]
	elif(recipient=="A-"):
		donors=["O-","A-"]
	elif(recipient=="B+"):
		donors=["O-","O+","B-","B+"]
	elif(recipient=="B-"):
		donors=["O-","B-"]
	elif(recipient=="O+"):
		donors=["O-","O+"]
	elif(recipient=="O-"):
		donors=["O-"]
	else:
		donors="Invalid input, restart the program"

	#print(f"Donors are: \n{donors}")
	for donor in donors:
		for i, row in df.iterrows():
			#print(f"donor is {donor}")
			#print(f"current blood type is {row[1]}")
			if (row[1]==donor and row[3]>=2):#							row[1] is the blood group row, row[3] is the health index, for healthy people, it should be greater than or equals to 2
				#print(f"A Person Named {row[0]} has blood_group is {row[1]} and their health is {row[3]} and their contact and address is : {row[4]}      {row[5]}")
				input_box.config(state= NORMAL)
				input_box.insert(END,f"A Person Named {row[0]} has blood_group is {row[1]} and their health is {row[3]} and their contact and address is : {row[4]}      {row[5]} \n")
				input_box.config(state= DISABLED)

df=pd.read_csv("data1.csv")

#donor_finder(recipient_input)

def on_submit():
	donor_input=e1.get()
	if(donor_input!=""):
		print(donor_input)
		recipient_finder(donor_input)
	recipient_input=e2.get()
	if(recipient_input!=""):
		print(recipient_input)
		donor_finder(recipient_input)

submit_button=Button(root,text="Submit",command=on_submit,bg="#000000",fg="#009999",font=("Orbitron",14)).pack(side=BOTTOM)

main_frame=LabelFrame(root,bg="#000000")
main_frame.pack(side=BOTTOM)

concept_checker=Label(main_frame, text="Concept Checker",bg="#000000",fg="#009999",font=("Orbitron",14))
concept_checker.grid(row=0,column=0)
e1=Entry(main_frame, bd=2,width=35, borderwidth=5, font=("Orbitron",14),bg="#000000",fg="#009999")
e1.grid(row=0,column=1)

donor_finder_label=Label(main_frame, text="Donor Finder",bg="#000000",fg="#009999",font=("Orbitron",14))
donor_finder_label.grid(row=1,column=0)
e2=Entry(main_frame,bd=2, width=35, borderwidth=5, font=("Orbitron",14),bg="#000000",fg="#009999")
e2.grid(row=1,column=1,pady=1)

root.mainloop()


