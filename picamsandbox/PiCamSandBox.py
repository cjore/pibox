#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PiCamCameraController import PiCamCameraController
from PiCamParamController import PiCamParamController

# Classe principale de l'application
class PiCamSandBox:
    # Constructeur
    def __init__(self):
        self.cameraController = PiCamCameraController()
        self.paramController = PiCamParamController(None)
        
    
if __name__ == "__main__":
    app = PiCamSandBox()
    #app.title('CameraParam')
    app.mainloop()
    app.destroy()
    
