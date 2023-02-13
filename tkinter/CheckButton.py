from tkinter import *

master = Tk()
checkbutton_value = BooleanVar()

checkbutton = Checkbutton(master, text= 'on/off', variable=checkbutton_value, height= 5 ).pack()
# height=5 aumenta a 'zona' clicável do checkbutton

mainloop()