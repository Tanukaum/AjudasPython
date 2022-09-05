import os
from tkinter import Button, StringVar, Tk
from tkinter import filedialog

def browseFile(path_origem):
        filetypes = [("PNG Files", "*.png ")]
        path = path_origem.get()
        
        if path:
            dir, base = os.path.split(path)
        
        opendialog = filedialog.Open(parent=root, filetypes=filetypes)
        file = opendialog.show(initialdir=dir, initialfile=base)

        #Se o caminho do arquivo for dentro da pasta desejada 
        #O path recebe o caminho do arquivo
        #Se não força o path a ter o caminho desejado
        if file[:"Numero de caracteres do path"] == "caminho da pasta desejada":
            path_origem.set(file)

        else:
            path_origem.set("caminho da pasta desejada/")
            
root = Tk()
path_origem = StringVar()
path_origem.set("Caminho da Pasta desejada")

Button(root, command= lambda:browseFile(path_origem)).pack()

root.mainloop()