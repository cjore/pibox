#!/usr/bin/python

from tkinter import *
from tkinter.messagebox import *
import picamera
from time import sleep

# Classe principale de l'application
class CameraParam(Tk):

    cameraEnable=True
   
    # Constructeur
    def __init__(self, parent):
        Tk.__init__(self,parent)
        self.parent = parent

    # Définition de la camera
    def definirCamera(self):
        try:
            camera = picamera.PiCamera()
        except picamera.exc.PiCameraError:
            self.cameraEnable=False
   
    # Définission de l'IHM
    def construireIHM(self):

        # Fenetre principale
        #fenetre = Tk()
        self.title='Test'

        self.attributes('-fullscreen',1)

        # Frame
        frameParametrage = Frame(self, bg="yellow", width=640, height=1080, padx=10, pady=10)
        frameParametrage.pack(side=RIGHT,fill=Y)

        frameParametrageHaut = Frame(frameParametrage, width=640, height=540)
        frameParametrageHaut.pack(side=TOP,fill=Y)

        frameParametrageBas = Frame(frameParametrage, width=640, height=540)
        frameParametrageBas.pack(side=BOTTOM,fill=Y)
    
        frameVisualisation = Frame(self, bg="blue",   width=1280, height=960)
        frameVisualisation.pack(side=TOP, fill=X)
    
        framePilotage = Frame(self, bg="red", width=1280, height=120, padx=10, pady=10)
        framePilotage.pack(side=BOTTOM, fill=X, expand=1)

        # Composant
        Canvas(frameVisualisation, width=1280, height=960, bg='ivory').pack(side=LEFT, padx=10, pady=10)

        l = LabelFrame(framePilotage, text="Pilotage")
        l.pack(side=TOP, fill=BOTH)

        # Boutons Preview
        Button(l, text='Start preview', command=self.startPreview).pack(side=LEFT, padx=5, pady=5)
        Button(l, text='Stop preview',command=self.stopPreview).pack(side=LEFT, padx=5, pady=5)

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
        sharpness.bind("<ButtonRelease>", self.reglerSharpness)

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

        # Bouton Exit
        Button(frameParametrageBas, text='Exit',command=self.quitApplication).pack(side=BOTTOM, padx=5, pady=5)

    # Lancement du preview
    def startPreview(self):
        texte = 'Start Preview\n'
        texte = texte + 'Sharpness : ' + valeurSharpness.get() + '\n'
        texte = texte + 'Contrast : ' + valeurContrast.get() + '\n'
        texte = texte + 'Brightness : ' + valeurBrightness.get() + '\n'
        texte = texte + 'Saturation : ' + valeurSaturation.get() + '\n'
        texte = texte + 'ISO : ' + valeurISO.get() + '\n'
        showinfo('Camera', texte)
        if cameraEnable:
            camera.start_preview(fullscreen=False, window=(35,10,1280,960))

    # Arrêt du preview
    def stopPreview(self):
        if cameraEnable:
            camera.stop_preview()

    # Fermeture de l'application
    def quitApplication(self):
        if self.cameraEnable:
            camera.stop_preview()
        self.quit()

    def reglerSharpness(event):
        #showinfo('Sharpness', valeurSharpness.get())
        camera.sharpness=valeurSharpness.get()

if __name__ == "__main__":
    app = CameraParam(None)
    app.title('CameraParam')
    app.definirCamera()
    app.construireIHM()
    app.mainloop()
    app.destroy()
