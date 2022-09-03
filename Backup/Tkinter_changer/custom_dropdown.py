from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define the style for combobox widget
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "orange", background= "white")

# Add a label widget
label=ttk.Label(win, text= "Select a Car Model",
font= ('Aerial 11'))
label.pack(pady=30)
# Add a Combobox widget
cb= ttk.Combobox(win, width= 25, values=["Honda", "Hyundai", "Wolkswagon", "Tata", "Renault", "Ford", "Chrevolet", "Suzuki","BMW", "Mercedes"])

cb.pack()

win.mainloop()