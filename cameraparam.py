#!/usr/bin/python

from tkinter import *
from tkinter.messagebox import *
import picamera
from time import sleep

def startPreview():
    texte = 'Start Preview\n'
    texte = texte + 'Sharpness : ' + valeurSharpness.get() + '\n'
    texte = texte + 'Contrast : ' + valeurContrast.get() + '\n'
    texte = texte + 'Brightness : ' + valeurBrightness.get() + '\n'
    texte = texte + 'Saturation : ' + valeurSaturation.get() + '\n'
    texte = texte + 'ISO : ' + valeurISO.get() + '\n'
    showinfo('Camera', texte)
    if cameraEnable:
        camera.start_preview(fullscreen=False, window=(35,10,1280,960))

def stopPreview():
    if cameraEnable:
        camera.stop_preview()

def quitApplication():
    if cameraEnable:
        camera.stop_preview()
    fenetre.quit()

def reglerSharpness(event):
    #showinfo('Sharpness', valeurSharpness.get())
    camera.sharpness=valeurSharpness.get()

fenetre = Tk()
fenetre.title='Test'

fenetre.attributes('-fullscreen',1)

cameraEnable=True

try:
    camera = picamera.PiCamera()
except picamera.exc.PiCameraError:
    cameraEnable=False

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

# Variables
valeurSharpness = StringVar()
valeurContrast = StringVar()
valeurBrightness = StringVar()
valeurBrightness.set(50)
valeurSaturation = StringVar()
valeurISO = StringVar()

# Params
Label(frameParametrageHaut, text="Sharpness :").grid(row=0,column=0)
sharpness = Scale(frameParametrageHaut, from_=-100, to=100, orient=HORIZONTAL, variable=valeurSharpness)
sharpness.grid(row=0,column=1)
sharpness.bind("<ButtonRelease>", reglerSharpness)

Label(frameParametrageHaut, text="Contrast :").grid(row=1,column=0)
contrast = Scale(frameParametrageHaut, from_=-100, to=100, orient=HORIZONTAL, variable=valeurContrast)
contrast.grid(row=1,column=1)

Label(frameParametrageHaut, text="Brightness :").grid(row=2,column=0)
brightness = Scale(frameParametrageHaut, from_=0, to=100, orient=HORIZONTAL, variable=valeurBrightness)
brightness.grid(row=2,column=1)

Label(frameParametrageHaut, text="Saturation :").grid(row=3,column=0)
saturation = Scale(frameParametrageHaut, from_=-100, to=100, orient=HORIZONTAL, variable=valeurSaturation)
saturation.grid(row=3,column=1)

Label(frameParametrageHaut, text="ISO :").grid(row=4,column=0)
iso = Scale(frameParametrageHaut, from_=0, to=800, orient=HORIZONTAL, variable=valeurISO)
iso.grid(row=4,column=1)

# Exit
Button(frameParametrageBas, text='Exit',command=quitApplication).pack(side=BOTTOM, padx=5, pady=5)

fenetre.mainloop()
fenetre.destroy()
