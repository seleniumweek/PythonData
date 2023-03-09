from tkinter import *
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.geometry('1000x600')
frame = Frame(root)
frame.pack()

greenbutton = Entry(frame, text="green", fg="green",width=100)
greenbutton.pack( side = BOTTOM )
ScrolledText(greenbutton).pack()

root.mainloop()