import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Notebook, Style
from tkinter import Frame

master = tk.Tk()

# Create an instance of ttk style
style = Style()
style.theme_use('default')
style.configure('.', background = '#ECF1F3')
style.configure('TNotebook.Tab', font='bold 20', background = '#f75c5c') #Vermelho
style.map('TNotebook.Tab', background = [("selected", "#96F7C5")]) #Verde

abas = Notebook(master)
frame_aba_1 = Frame(abas)        
frame_aba_2 = Frame(abas)
frame_aba_3 = Frame(abas)
frame_aba_4 = Frame(abas)
frame_aba_5 = Frame(abas)
frame_aba_6 = Frame(abas)
abas.add(frame_aba_1,text="Formação 1")
abas.add(frame_aba_2,text="Formação 2")
abas.add(frame_aba_3,text="Formação 3")
abas.add(frame_aba_4,text="Formação 4")
abas.pack(fill="both",expand=1)

master.mainloop()