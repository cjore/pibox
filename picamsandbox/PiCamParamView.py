#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from PiCamParamModel import PiCamParamModel

# Vue du module de paramétrage
class PiCamParamView(Tk):

    # Constructeur
    def __init__(self, parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.paramModel = PiCamParamModel(self)
        self.construireIHM()

         # Définission de l'IHM
    def construireIHM(self):

        # Fenetre principale
        self.title='Test'

        self.attributes('-fullscreen',1)

        # Frame
        frameParametrage = Frame(self, bg="yellow", width=640, height=800, padx=10, pady=10)
        frameParametrage.pack(side=RIGHT,fill=Y)

        frameParametrageHaut = Frame(frameParametrage, width=640, height=400)
        frameParametrageHaut.pack(side=TOP,fill=Y)

        frameParametrageBas = Frame(frameParametrage, width=640, height=400)
        frameParametrageBas.pack(side=BOTTOM,fill=Y)
    
        frameVisualisation = Frame(self, bg="blue",   width=1280, height=800)
        frameVisualisation.pack(side=TOP, fill=X)
    
        framePilotage = Frame(self, bg="red", width=1280, height=120, padx=10, pady=10)
        framePilotage.pack(side=BOTTOM, fill=X, expand=1)

        # Composant
        Canvas(frameVisualisation, width=1280, height=800, bg='ivory').pack(side=LEFT, padx=10, pady=10)

        l = LabelFrame(framePilotage, text="Pilotage")
        l.pack(side=TOP, fill=BOTH)

        # Boutons Preview
        Button(l, text='Start preview', command=self.startPreview).pack(side=LEFT, padx=5, pady=5)
        Button(l, text='Stop preview',command=self.stopPreview).pack(side=LEFT, padx=5, pady=5)

        # Params
        Label(frameParametrageHaut, text="Sharpness :").grid(row=0,column=0,sticky=W)
        sharpness = Scale(frameParametrageHaut, from_=-100, to=100, orient=HORIZONTAL, variable=self.valeurSharpness)
        sharpness.grid(row=0,column=1)
        sharpness.bind("<B1-Motion>", self.reglerSharpness)

        Label(frameParametrageHaut, text="Contrast :").grid(row=1,column=0,sticky=W)
        contrast = Scale(frameParametrageHaut, from_=-100, to=100, orient=HORIZONTAL, variable=self.valeurContrast)
        contrast.grid(row=1,column=1)
        contrast.bind("<B1-Motion>", self.reglerContrast)

        Label(frameParametrageHaut, text="Brightness :").grid(row=2,column=0,sticky=W)
        brightness = Scale(frameParametrageHaut, from_=0, to=100, orient=HORIZONTAL, variable=self.valeurBrightness)
        brightness.grid(row=2,column=1)
        brightness.bind("<B1-Motion>", self.reglerBrightness)

        Label(frameParametrageHaut, text="Saturation :").grid(row=3,column=0,sticky=W)
        saturation = Scale(frameParametrageHaut, from_=-100, to=100, orient=HORIZONTAL, variable=self.valeurSaturation)
        saturation.grid(row=3,column=1)
        saturation.bind("<B1-Motion>", self.reglerSaturation)

        Label(frameParametrageHaut, text="ISO :").grid(row=4,column=0,sticky=W)
        iso = Scale(frameParametrageHaut, from_=0, to=800, orient=HORIZONTAL, variable=self.valeurISO)
        iso.grid(row=4,column=1)
        iso.bind("<B1-Motion>", self.reglerIso)

        stabilisationLF = LabelFrame(frameParametrageHaut, text="Stabilisation :")
        stabilisationLF.grid(columnspan=2, sticky=W)
        Radiobutton(stabilisationLF, text="Oui", variable=self.valeurStabilisation, value=True, command=self.choisirStabilisation).grid(row=0,column=0)
        Radiobutton(stabilisationLF, text="Non", variable=self.valeurStabilisation, value=False, command=self.choisirStabilisation).grid(row=0,column=1)

        Label(frameParametrageHaut, text="Exposure compensation :").grid(row=6,column=0,sticky=W)
        exCompensation = Scale(frameParametrageHaut, from_=-25, to=25, orient=HORIZONTAL, variable=self.valeurExCompensation)
        exCompensation.grid(row=6,column=1)
        exCompensation.bind("<B1-Motion>", self.reglerExCompensation)

        Label(frameParametrageHaut, text="Exposure mode :").grid(row=7,column=0,sticky=W)
        exMode = ttk.Combobox(frameParametrageHaut, textvariable=self.valeurExMode)
        exMode.grid(row=7,column=1)
        exMode['values'] = ['auto','off','night','nightpreview','backlight','sports','snom','beach','verylong','fixedfps','antishake','fireworks']
        exMode.bind("<<ComboboxSelected>>", self.reglerExMode) 

        Label(frameParametrageHaut, text="Flash mode :").grid(row=8,column=0,sticky=W)
        exMode = ttk.Combobox(frameParametrageHaut, textvariable=self.valeurFlashMode)
        exMode.grid(row=8,column=1)
        exMode['values'] = ['off','auto','on','redeye','fillin','torch']
        exMode.bind("<<ComboboxSelected>>", self.reglerFlashMode)

        hflipLF = LabelFrame(frameParametrageHaut, text="HFlip :")
        hflipLF.grid(columnspan=2, sticky=W)
        Radiobutton(hflipLF, text="Oui", variable=self.valeurHFlip, value=True, command=self.choisirHFlip).grid(row=0,column=0)
        Radiobutton(hflipLF, text="Non", variable=self.valeurHFlip, value=False, command=self.choisirHFlip).grid(row=0,column=1)

        vflipLF = LabelFrame(frameParametrageHaut, text="VFlip :")
        vflipLF.grid(columnspan=2, sticky=W)
        Radiobutton(vflipLF, text="Oui", variable=self.valeurVFlip, value=True, command=self.choisirVFlip).grid(row=0,column=0)
        Radiobutton(vflipLF, text="Non", variable=self.valeurVFlip, value=False, command=self.choisirVFlip).grid(row=0,column=1)

        Label(frameParametrageHaut, text="Image effect :").grid(row=11,column=0,sticky=W)
        exMode = ttk.Combobox(frameParametrageHaut, textvariable=self.valeurImageEffect)
        exMode.grid(row=11,column=1)
        exMode['values'] = ['none','negative','solarize','sketch','denoise','emboss','oilpaint','hatch','gpen','pastel','watercolor','film','blur','saturation','colorswap','washedout','posterise','colorpoint','colorbalance','cartoon','deinterlace1','deinterlace2']
        exMode.bind("<<ComboboxSelected>>", self.reglerImageEffect)

        Label(frameParametrageHaut, text="Zoom :").grid(row=12,column=0,sticky=W)
        exCompensation = Scale(frameParametrageHaut, from_=1.0, to=0.1, resolution=0.1, orient=HORIZONTAL, variable=self.valeurZoom)
        exCompensation.grid(row=12,column=1)
        exCompensation.bind("<B1-Motion>", self.reglerZoom)

        # Bouton Exit
        Button(frameParametrageBas, text='Exit',command=self.quitApplication).pack(side=BOTTOM, padx=5, pady=5)

        
