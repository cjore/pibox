#!/usr/bin/python3
# -*- coding: utf-8 -*-

from imutils.video.pivideostream import PiVideoStream
#from PiVideoStream import PiVideoStream
import cv2
import time
import imutils

# created a "threaded" video stream, allow the camera sensor to warmup
vs = PiVideoStream((1280, 720)).start()
time.sleep(1.0)

# Lecture de l'image
reticule = cv2.imread("target-red.png")
reticule = imutils.resize(reticule, width=100)
rows, cols, channels = reticule.shape

# Masks creation
grayreticule = cv2.cvtColor(reticule, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(grayreticule, 127, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Loop over the frames of the video
while True :

	# grab the current frame
	frame = vs.read()
	
	frame2 = imutils.resize(frame, width=1280)
	#reticule = imutils.resize(reticule, width=50)
	
	#grayreticule = cv2.cvtColor(reticule, cv2.COLOR_BGR2GRAY)
	#grayframe = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
	
	#x_offset=y_offset=50
	#grayframe[y_offset:y_offset+reticule.shape[0], x_offset:x_offset+reticule.shape[1]] = grayreticule
	
	# ROI definition
	roi = frame2[0:rows, 0:cols]

	# black-out the area of reticule in ROI
	frame_bg = cv2.bitwise_and(roi, roi, mask = mask)
	#print(frame_bg.shape)
	
	# take only region of reticule from reticule image
	reticule_fg = cv2.bitwise_and(reticule, reticule, mask = mask_inv)
	#print(reticule_fg.shape)
	
	# put logo in ROI and modify the main frame
	dst = cv2.add(frame_bg, reticule_fg)
	frame2[0:rows, 0:cols] = dst
		
	# show the frame 
	cv2.imshow("Target", frame2)
		
	# wait user action
	key = cv2.waitKey(1) & 0xFF
		
	# if the 'q' key is pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
