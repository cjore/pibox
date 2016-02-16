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
        self.definirCamera()
        self.construireIHM()

    # Définition de la camera
    def definirCamera(self):
        try:
            self.camera = picamera.PiCamera()
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
        self.valeurSharpness = StringVar()
        self.valeurContrast = StringVar()
        self.valeurBrightness = StringVar()
        self.valeurBrightness.set(50)
        self.valeurSaturation = StringVar()
        self.valeurISO = StringVar()
        self.valeurStabilisation = IntVar()

        # Params
        Label(frameParametrageHaut, text="Sharpness :").grid(row=0,column=0)
        sharpness = Scale(frameParametrageHaut, from_=-100, to=100, orient=HORIZONTAL, variable=self.valeurSharpness)
        sharpness.grid(row=0,column=1)
        sharpness.bind("<B1-Motion>", self.reglerSharpness)

        Label(frameParametrageHaut, text="Contrast :").grid(row=1,column=0)
        contrast = Scale(frameParametrageHaut, from_=-100, to=100, orient=HORIZONTAL, variable=self.valeurContrast)
        contrast.grid(row=1,column=1)
        contrast.bind("<B1-Motion>", self.reglerContrast)

        Label(frameParametrageHaut, text="Brightness :").grid(row=2,column=0)
        brightness = Scale(frameParametrageHaut, from_=0, to=100, orient=HORIZONTAL, variable=self.valeurBrightness)
        brightness.grid(row=2,column=1)
        brightness.bind("<B1-Motion>", self.reglerBrightness)

        Label(frameParametrageHaut, text="Saturation :").grid(row=3,column=0)
        saturation = Scale(frameParametrageHaut, from_=-100, to=100, orient=HORIZONTAL, variable=self.valeurSaturation)
        saturation.grid(row=3,column=1)
        saturation.bind("<B1-Motion>", self.reglerSaturation)

        Label(frameParametrageHaut, text="ISO :").grid(row=4,column=0)
        iso = Scale(frameParametrageHaut, from_=0, to=800, orient=HORIZONTAL, variable=self.valeurISO)
        iso.grid(row=4,column=1)
        iso.bind("<B1-Motion>", self.reglerIso)

        stabilisationLF = LabelFrame(frameParametrageHaut, text="Stabilisation")
        Radiobutton(stabilisationLF, text="Oui", variable=valeurStabilisation, value=True)
        Radiobutton(stabilisationLF, text="Non", variable=valeurStabilisation, value=False)

        # Bouton Exit
        Button(frameParametrageBas, text='Exit',command=self.quitApplication).pack(side=BOTTOM, padx=5, pady=5)

    # Lancement du preview
    def startPreview(self):
        texte = 'Start Preview\n'
        texte = texte + 'Sharpness : ' + self.valeurSharpness.get() + '\n'
        texte = texte + 'Contrast : ' + self.valeurContrast.get() + '\n'
        texte = texte + 'Brightness : ' + self.valeurBrightness.get() + '\n'
        texte = texte + 'Saturation : ' + self.valeurSaturation.get() + '\n'
        texte = texte + 'ISO : ' + self.valeurISO.get() + '\n'
        #showinfo('Camera', texte)
        if self.cameraEnable:
            self.camera.start_preview(fullscreen=False, window=(35,10,1280,960))

    # Arrêt du preview
    def stopPreview(self):
        if self.cameraEnable:
            self.camera.stop_preview()

    # Fermeture de l'application
    def quitApplication(self):
        if self.cameraEnable:
            self.camera.stop_preview()
        self.quit()

    def reglerSharpness(self,event):
        #showinfo('Sharpness', self.valeurSharpness.get())
        if self.cameraEnable:
            self.camera.sharpness=int(self.valeurSharpness.get())

    def reglerContrast(self,event):
        if self.cameraEnable:
            self.camera.contrast=int(self.valeurContrast.get())

    def reglerBrightness(self,event):
        if self.cameraEnable:
            self.camera.brightness=int(self.valeurBrightness.get())

    def reglerSaturation(self,event):
        if self.cameraEnable:
            self.camera.saturation=int(self.valeurSaturation.get())

    def reglerIso(self,event):
        if self.cameraEnable:
            self.camera.ISO=int(self.valeurISO.get())        
        

if __name__ == "__main__":
    app = CameraParam(None)
    #app.title('CameraParam')
    app.mainloop()
    app.destroy()
