import tkinter

from tkinter import * #this means from tkinter you import everything

win = Tk()

b = 0
for i in range(6):
    for j in range(6):
        b = b + 1
        Button(win, text=str(b), borderwidth=1).grid(row=i, column=j)

win.mainloop()