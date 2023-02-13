import tkinter as tk
from PIL import Image, ImageTk

master = tk.Tk()
label_img = tk.Label(master, text= 'empty')
label_img.grid(column=1, row=1)



def change_img(): 
    #Carrega a imagem
    image_open = Image.open(r'Imgs\images.jpg')
    #Converte a image em TkImage
    image_convert= ImageTk.PhotoImage(image_open)
    label_img.configure(image=image_convert)
    label_img.image = image_convert

def change_img2(): 
    #Carrega a imagem
    image_open = Image.open(r'Imgs\images2.jpg')
    #Converte a image em TkImage
    image_convert= ImageTk.PhotoImage(image_open)
    label_img.configure(image=image_convert)
    label_img.image = image_convert


tk.Button(master,text='Change Label' , command = lambda: change_img()).grid(column=2, row=1)
tk.Button(master,text='Change Label2' , command = lambda: change_img2()).grid(column=2, row=2)





master.mainloop()