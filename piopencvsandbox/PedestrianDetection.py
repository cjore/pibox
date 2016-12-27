#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import the necessary package
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils.video.pivideostream import PiVideoStream
from imutils import paths
import numpy as np
import imutils
import cv2
import time

# Initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# created a "threaded" video stream, allow the camera sensor to warmup
vs = PiVideoStream().start()
time.sleep(1.0)

# Loop over the frames of the video
while True :
		
	# grab the current frame and resize it to (1) reduce detection time and (2) improve detection accuracy
	frame = vs.read()
	image = imutils.resize(frame, width=320)
	orig = image.copy()
	
	# detect people in the image
	(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05) 

	# draw the original bounding boxes
	for (x, y, w, h) in rects:
		cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)
		
	# apply non-maxima suppression to the bounding boxes using a fairly large overlap thresold to try 
	# to maintain overlapping boxes that are still people
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
	
	# draw the final bounding boxes 
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
		
	# show some information on the number of bounding boxes
	if (len(pick) > 0) :
		print("[INFO] : {} original boxes, {} after suppression".format(len(rects), len(pick)))	 

	#show the output images
	#cv2.imshow("Before NMS", orig)
	cv2.imshow("After NMS", image)

	# wait user action
	key = cv2.waitKey(1) & 0xFF
		
	# if the 'q' key is pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
