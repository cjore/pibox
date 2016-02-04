#!/usr/bin/python

import picamera
from time import sleep

camera = picamera.PiCamera()
#camera.resolution = (1280,720)
camera.start_preview(fullscreen=False, window=(100,20,1280,960))
camera.annotate_background = picamera.Color('black')
camera.annotate_text='Hello World'
sleep(5)
camera.stop_preview()
