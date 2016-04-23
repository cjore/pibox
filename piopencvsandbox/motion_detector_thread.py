#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
#from picamera.array import PiRGBArray
#from picamera import PiCamera
import argparse
import datetime
import imutils
import time
import cv2

# initialize the camera and stream
#camera = PiCamera()
#camera.resolution = (320, 240)
#camera.framerate = 32
#rawCapture = PiRGBArray(camera, size=(320, 240))
#stream = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

# created a "threaded" video stream, allow the camera sensor to warmup, and start the FPS counter
print("[INFO] sampling THREAD frames from picamera module");
vs = PiVideoStream().start()
time.sleep(2.0)
fps = FPS().start()

# Initialize the first fram in the video stream
firstFrame = None

# Loop over the frames of the video
while True :
	# grab the current frame ans initialize the occupied/unoccupied test
	frame = vs.read()
	text = "Unocoppied"
	
	# resize the frame, convert it to greyscale, and blur it
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21,21), 0)
	
	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue
		
	# compute the absolute difference between the current frame and first frame
	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	
	# dilate the thresolded image to fill in holes, then find contours on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)
	(_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	
	# loop over the contours
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < args["min_area"]:
			continue
			
		# compute the bounding box for the contour, draw it on the frame, and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		text = "Occupied"	 	
				
	# draw the text and timestamp on the frame
	cv2.putText(frame, "Room Status: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
	
	# show the frameand record if the user presses a key
	cv2.imshow("Security Feed", frame)
	cv2.imshow("Thresh", thresh)
	cv2.imshow("Frame Delta", frameDelta)
	key = cv2.waitKey(1) & 0xFF
	
	fps.update()
		
	# if the 'q' key is pressed, break from the loop
	if key == ord("q"):
		break

fps.stop()
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
