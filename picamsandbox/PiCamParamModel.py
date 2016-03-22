#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Model du module de paramétrage
class PiCamParamModel():

    def __init__(self):
        # Variables
        self.valeurSharpness = StringVar()
        self.valeurContrast = StringVar()
        self.valeurBrightness = StringVar()
        self.valeurBrightness.set(50)
        self.valeurSaturation = StringVar()
        self.valeurISO = StringVar()
        self.valeurStabilisation = BooleanVar()
        self.valeurExCompensation = IntVar()
        self.valeurExMode = StringVar()
        self.valeurExMode.set('auto')
        self.valeurFlashMode = StringVar()
        self.valeurFlashMode.set('off')
        self.valeurHFlip = BooleanVar()
        self.valeurVFlip = BooleanVar()
        self.valeurImageEffect = StringVar()
        self.valeurImageEffect.set('none')
        self.valeurZoom = DoubleVar()
        self.valeurZoom.set(1.0)
