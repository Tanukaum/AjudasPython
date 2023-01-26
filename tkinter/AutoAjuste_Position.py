from tkinter import *

root = Tk()
root.title("AutoAjuste.py")
frame_AB = Frame(root)
frame_A = LabelFrame(frame_AB,text="A")
frame_B = LabelFrame(frame_AB,text="B")

frame_CE = Frame(root)
frame_C = LabelFrame(frame_CE,text="C")
frame_D = LabelFrame(frame_AB,text="D")
frame_E = LabelFrame(frame_CE,text="E")

label= Label(frame_A,text="Label A",justify=LEFT)
label.pack(side=LEFT)

label= Label(frame_B,text="Label B",justify=LEFT)
label.pack(side=LEFT)

label= Label(frame_C,text="Label C",justify=LEFT)
label.pack(side=LEFT)

label= Label(frame_D,text="Label D",justify=LEFT)
label.pack(side=LEFT)

label= Label(frame_E,text="Label E",justify=LEFT)
label.pack(side=LEFT)

frame_A.pack(side='left')
frame_B.pack(side='left')
frame_C.pack(side='left')
frame_D.pack()
frame_E.pack(side='left')

frame_AB.pack()
frame_CE.pack()
root.mainloop()