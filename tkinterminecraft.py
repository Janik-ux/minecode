from mcpi.minecraft import Minecraft
from tkinter import *

import time
import os

def option1():
    x = str(dateinam.get())
    print(x)

mc = Minecraft.create()
fen = Tk()
dateinam = StringVar()

fen.title("Minecraftprogramm")
fen.geometry("300x300")

beg  = Label(fen, text="Hallo! Geben Sie einen Projektnamen ein.")
ein  = Entry(fen, textvariable=dateinam)
btn1 = Button(fen, text="Eingeben", command=option1)

beg.pack()
ein.pack()
btn1.pack()
fen.mainloop()