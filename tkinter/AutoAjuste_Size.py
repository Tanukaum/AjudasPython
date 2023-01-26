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
label.pack(side=LEFT, fill='both', expand=1)

label= Label(frame_B,text="Label B",justify=LEFT)
label.pack(side=LEFT, fill='both', expand=1)

label= Label(frame_C,text="Label C",justify=LEFT)
label.pack(side=LEFT, fill='both', expand=1)

label= Label(frame_D,text="Label D",justify=LEFT)
label.pack(side=LEFT, fill='both', expand=1)

label= Label(frame_E,text="Label E",justify=LEFT)
label.pack(side=LEFT, fill='both', expand=1)

frame_A.pack(side='left', fill='both', expand=1)
frame_B.pack(side='left', fill='both', expand=1)
frame_C.pack(side='left', fill='both', expand=1)
frame_D.pack(fill='both', expand=1)
frame_E.pack(side='left', fill='both', expand=1)

frame_AB.pack( fill='both', expand=1)
frame_CE.pack(fill='both', expand=1)
root.mainloop()