#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from PiCamCameraController import PiCamCameraController
from PiCamParamController import PiCamParamController

# Classe principale de l'application
class PiCamSandBox:
    # Constructeur
    def __init__(self, root):
        self.cameraController = PiCamCameraController()
        self.paramController = PiCamParamController(root, self.cameraController)
        
    def mainloop(self):
        self.paramController.paramView.mainloop()
    
if __name__ == "__main__":
    root = Tk()
    app = PiCamSandBox(root)
    #app.title('CameraParam')
    root.mainloop()
    root.destroy()
    
