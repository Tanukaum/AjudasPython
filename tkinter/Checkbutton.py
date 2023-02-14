from tkinter import *

def on_change():
    print(check_var.get())
    if check_var.get():
        print('1')
    else:
        print('0')

master = Tk()
check_var = BooleanVar()

Checkbutton(master, text='on/off', variable=check_var, command=on_change, height=5).pack()
#height=5 aumenta a 'zona' clicável do checkbutton

master.mainloop()