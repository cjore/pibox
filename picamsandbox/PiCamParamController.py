#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PiCamParamView import PiCamParamView

# Vue du module de d'enregistrement
class PiCamParamController:

    # Constructeur
    def __init__(self, parent):
        self.parent = parent
        #self.paramModel = PiCamParamModel(parent)
        self.paramView = PiCamParamView(parent)

    # Fermeture de l'application
    def quitApplication(self):
        if self.cameraEnable:
            self.camera.stop_preview()
        self.quit()

    def reglerSharpness(self,event):
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

    def choisirStabilisation(self):
        showinfo('Stabilisation', self.valeurStabilisation.get())
        if self.cameraEnable:
            self.camera.video_stabilization = self.valeurStabilisation.get()

    def reglerExCompensation(self,event):
        if self.cameraEnable:
            self.camera.exposure_compensation=int(self.valeurExCompensation.get())

    def reglerExMode(self,event):
        if self.cameraEnable:
            self.camera.exposure_mode=self.valeurExMode.get()        

    def reglerFlashMode(self,event):
        if self.cameraEnable:
            self.camera.flash_mode=self.valeurFlashMode.get()

    def choisirHFlip(self):
        if self.cameraEnable:
            self.camera.hflip = self.valeurHFlip.get()

    def choisirVFlip(self):
        if self.cameraEnable:
            self.camera.vflip = self.valeurVFlip.get()

    def reglerImageEffect(self, event):
        if self.cameraEnable:
            self.camera.image_effect=self.valeurImageEffect.get()

    def reglerZoom(self,event):
        if self.cameraEnable:
            self.camera.zoom = (0.0,0.0,self.valeurZoom.get(),self.valeurZoom.get())        
