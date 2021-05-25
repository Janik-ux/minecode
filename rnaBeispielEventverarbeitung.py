from tkinter import *
def linksklick(event):
    event.widget.config(bg='green')
def rechtsklick(event):
    event.widget.config(bg='blue')
def doppelklick(event):
    event.widget.config(bg='white')
liste=[(x,y) for x in range(10) for y in range(10)]
fenster = Tk()
for (i,j) in liste:
    l=Label(fenster, width=2, height=1, bg='white')
    l.grid(column=i, row=j)
    l.bind(sequence='<Button-1>', func=linksklick)
    l.bind(sequence='<Button-3>', func=rechtsklick)
    l.bind(sequence='<Double-Button-1>', func=doppelklick)
    fenster.mainloop()