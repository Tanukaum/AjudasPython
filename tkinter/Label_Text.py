from tkinter import *

master = Tk()
label_var = StringVar()
label = Label(master, textvariable=label_var).pack()

def msg():
    label_var.set('Olá Mundo')

button = Button(master, text="Mostrar Mensagem", command=msg)
button.pack()

mainloop()