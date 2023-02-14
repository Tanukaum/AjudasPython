import os
from tkinter import *

path_folder = r'C:\Users\Public\Documents'
file_list = os.listdir(path_folder)

master = Tk()

file_path = StringVar(master)
file_path.set(file_list[0]) # default value

drop_list = OptionMenu(master, file_path, *file_list)
drop_list.pack()
drop_list.config(font='bold 13') #Fonte da caixa

drop_config = master.nametowidget(drop_list.menuname)  # Get menu widget.
drop_config.config(font='bold 13')  # Fonte da lista

def file():
    print ("File is:" + file_path.get())

button = Button(master, text="FILE?", command=file)
button.pack()

mainloop()