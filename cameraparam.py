#!/usr/bin/python

from tkinter import *
from tkinter.messagebox import *

def startPreview():
    showinfo('Camera', 'Start Preview')

def stopPreview():
    showinfo('Camera', 'Stop Preview')  

fenetre = Tk()
fenetre.title='Test'

fenetre.attributes('-fullscreen',1)

# Frame
frameParametrage = Frame(fenetre, bg="yellow", width=640, height=1080, padx=10, pady=10)
frameParametrage.pack(side=RIGHT,fill=Y)

frameParametrageHaut = Frame(frameParametrage, width=640, height=540)
frameParametrageHaut.pack(side=TOP,fill=Y)

frameParametrageBas = Frame(frameParametrage, width=640, height=540)
frameParametrageBas.pack(side=BOTTOM,fill=Y)
    
frameVisualisation = Frame(fenetre, bg="blue",   width=1280, height=960)
frameVisualisation.pack(side=TOP, fill=X)
    
framePilotage = Frame(fenetre, bg="red", width=1280, height=120, padx=10, pady=10)
framePilotage.pack(side=BOTTOM, fill=X, expand=1)

Canvas(frameVisualisation, width=1280, height=960, bg='ivory').pack(side=LEFT, padx=10, pady=10)

l = LabelFrame(framePilotage, text="Pilotage")
l.pack(side=TOP, fill=BOTH)

# Preview
Button(l, text='Start preview', command=startPreview).pack(side=LEFT, padx=5, pady=5)
Button(l, text='Stop preview',command=stopPreview).pack(side=LEFT, padx=5, pady=5)

# Params
lab1 = Label(frameParametrageHaut, text="Sharpness :").grid(row=0,column=0)
ent1 = Entry(frameParametrageHaut).grid(row=0,column=1)
lab2 = Label(frameParametrageHaut, text="Contrast :").grid(row=1,column=0)
ent2 = Entry(frameParametrageHaut).grid(row=1,column=1)
lab3 = Label(frameParametrageHaut, text="Brightness :").grid(row=2,column=0)
ent3 = Entry(frameParametrageHaut).grid(row=2,column=1)
lab4 = Label(frameParametrageHaut, text="Saturation :").grid(row=3,column=0)
ent4 = Entry(frameParametrageHaut).grid(row=3,column=1)
lab5 = Label(frameParametrageHaut, text="ISO :").grid(row=4,column=0)
ent5 = Entry(frameParametrageHaut).grid(row=4,column=1)

# Exit
Button(frameParametrageBas, text='Quit',command=fenetre.quit).pack(side=BOTTOM, padx=5, pady=5)

fenetre.mainloop()
