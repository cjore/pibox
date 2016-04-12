#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PiCamParamView import PiCamParamView
from PiCamParamModel import PiCamParamModel

# Vue du module de d'enregistrement
class PiCamParamController:

    # Constructeur
    def __init__(self, parent, camController):
        self.parent = parent
        self.paramModel = PiCamParamModel(parent)
        self.paramView = PiCamParamView(parent, self, self.paramModel, camController)
        self.camController = camController
        self.camModel = self.camController.cameraModel

    # Fermeture de l'application
    def quitApplication(self):
        if self.camModel.cameraEnable:
            self.camController.camera.stop_preview()
        self.paramView.parent.quit()

    def reglerSharpness(self,event):
        if self.camModel.cameraEnable:
            self.camController.camera.sharpness=int(self.paramModel.valeurSharpness.get())

    def reglerContrast(self,event):
        if self.camModel.cameraEnable:
            self.camController.camera.contrast=int(self.paramModel.valeurContrast.get())

    def reglerBrightness(self,event):
        if self.camModel.cameraEnable:
            self.camController.camera.brightness=int(self.paramModel.valeurBrightness.get())

    def reglerSaturation(self,event):
        if self.camModel.cameraEnable:
            self.camController.camera.saturation=int(self.paramModel.valeurSaturation.get())

    def reglerIso(self,event):
        if self.camModel.cameraEnable:
            self.camController.camera.ISO=int(self.paramModel.valeurISO.get())

    def choisirStabilisation(self):
        if self.camModel.cameraEnable:
            self.camController.camera.video_stabilization = self.paramModel.valeurStabilisation.get()

    def reglerExCompensation(self,event):
        if self.camModel.cameraEnable:
            self.camController.camera.exposure_compensation=int(self.paramModel.valeurExCompensation.get())

    def reglerExMode(self,event):
        if self.camModel.cameraEnable:
            self.camController.camera.exposure_mode=self.paramModel.valeurExMode.get()        

    def reglerFlashMode(self,event):
        if self.camModel.cameraEnable:
            self.camController.camera.flash_mode=self.paramModel.valeurFlashMode.get()

    def choisirHFlip(self):
        if self.camModel.cameraEnable:
            self.camController.camera.hflip = self.paramModel.valeurHFlip.get()

    def choisirVFlip(self):
        if self.camModel.cameraEnable:
            self.camController.camera.vflip = self.paramModel.valeurVFlip.get()

    def reglerImageEffect(self, event):
        if self.camModel.cameraEnable:
            self.camController.camera.image_effect=self.paramModel.valeurImageEffect.get()

    def reglerZoom(self,event):
        if self.camModel.cameraEnable:
            self.camController.camera.zoom = (0.0,0.0,self.paramModel.valeurZoom.get(),self.paramModel.valeurZoom.get())        
