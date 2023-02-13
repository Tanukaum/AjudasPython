import tkinter as tk
from tkinter import *

def on_change():
    print(check_var.get())
    if check_var.get():
        print('1')
    else:
        print('0')

root = tk.Tk()
check_var = tk.BooleanVar()
tk.Checkbutton(root, text='on/off', variable=check_var, command=on_change).pack()
root.mainloop()

