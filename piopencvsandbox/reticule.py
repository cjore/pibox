#!/usr/bin/python3
# -*- coding: utf-8 -*-

from imutils.video.pivideostream import PiVideoStream
#from PiVideoStream import PiVideoStream
import cv2
import time
import imutils

mx = 50
my = 50
mxcourant = mx
mycourant = my

# mouse callback function
def moveTarget(event,x,y,flags,param):
	if event == cv2.EVENT_MOUSEMOVE :
		global mx
		global my
		#mx = int(x/10)
		#my = int(y/10)
		
		if (x - 50 < 0):
			mx = 0 
		elif (x + 100 > 1280):
			mx = 1280 -100
		else:
			mx = x - 50
	
		
		if (y - 50 < 0): 
			my = 0
		elif (y + 100 > 720):	
			my = 720 - 100
		else:
			my = y - 50	
		print('x : ' + str(x) + " - " + " y : " + str(y))
		
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

	# ROI definition
	roi = frame2[my:rows+my, mx:cols+mx]
	
	print('mx : ' + str(mx) + " - my : " + str(my) + " - rows : " +  str(rows+mx) + " - cols : " + str(cols+my))
	
	# black-out the area of reticule in ROI
	frame_bg = cv2.bitwise_and(roi, roi, mask = mask)
	#print(frame_bg.shape)
	
	# take only region of reticule from reticule image
	reticule_fg = cv2.bitwise_and(reticule, reticule, mask = mask_inv)
	#print(reticule_fg.shape)
	
	# put logo in ROI and modify the main frame
	dst = cv2.add(frame_bg, reticule_fg)
	frame2[my:rows+my, mx:cols+mx] = dst
		
	# show the frame 
	cv2.imshow("Target", frame2)
	
	
	cv2.setMouseCallback("Target", moveTarget)
		
	# wait user action
	key = cv2.waitKey(1) & 0xFF
		
	# if the 'q' key is pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
