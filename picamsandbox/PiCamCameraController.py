#!/usr/bin/python3
# -*- coding: utf-8 -*-

import picamera
from PiCamCameraModel import PiCamCameraModel

class PiCamCameraController():

    def __init__(self):
        self.cameraModel = PiCamCameraModel()
        try:
            self.camera = picamera.PiCamera()
        except picamera.exc.PiCameraError:
            self.cameraModel.cameraEnable=False

    # Lancement du preview
    def startPreview(self):
        if self.cameraModel.cameraEnable:
            self.camera.video_stabilization = True;
            self.camera.start_preview(fullscreen=False, window=(83,10,1280,960))

    # Arrêt du preview
    def stopPreview(self):
        if self.cameraModel.cameraEnable:
            self.camera.stop_preview()            
