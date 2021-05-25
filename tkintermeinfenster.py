from tkinter import *
from tkinter import messagebox
import time

def sel():
    selection = str(var.get())
    print(selection)


a = Tk()
a.title("Erstes interaktives Programm")

##Alter = input("Bitte geben Sie Ihr Alter an!")
##Alter = int(Alter)
##
##if Alter in range(1, 6):
##    antwort1 = input("Dürfen Sie überhaupt an diesen Computer?")
##    if antwort1 == "nein" :
##        Pinabfrage = input("Bitte geben Sie den Pin ein!")
##        while Pinabfrage != "7477" :
##            print("Pin falsch!")
##            time.sleep(1)
##            Pinabfrage = input("Bitte geben Sie den Pin ein!")
##        else:
##            print("Programm entsperrt")
##else:
##
##     None
var = DoubleVar()
scroll = Scale(a, from_=130, to= 0, variable=var)
btn = Button(a, text="Eingeben", command=sel)
scroll.pack()
btn.pack()
a = mainloop()