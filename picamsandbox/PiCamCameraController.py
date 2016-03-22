#!/usr/bin/python3
# -*- coding: utf-8 -*-

class PiCamCameraController():

    def __init__(self):
        try:
            self.camera = picamera.PiCamera()
        except picamera.exc.PiCameraError:
            self.cameraEnable=False

    # Lancement du preview
    def startPreview(self):
        if self.cameraEnable:
            self.camera.video_stabilization = True;
            self.camera.start_preview(fullscreen=False, window=(83,10,1280,960))

    # Arrêt du preview
    def stopPreview(self):
        if self.cameraEnable:
            self.camera.stop_preview()            
