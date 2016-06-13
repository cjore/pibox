#!/usr/bin/python3
# -*- coding: utf-8 -*-

from imutils.video.pivideostream import PiVideoStream
#from PiVideoStream import PiVideoStream
import cv2
import time
import imutils

mx = 50
my = 50
resolutionx = 480
resolutiony = 360
widthTarget = 75
halfWidthTarget = int(widthTarget/2)

# mouse callback function
def moveTarget(event,x,y,flags,param):
	if event == cv2.EVENT_MOUSEMOVE :
		global mx
		global my
		
		if (x - halfWidthTarget < 0):
			mx = 0 
		elif (x + widthTarget > resolutionx):
			mx = resolutionx -widthTarget
		else:
			mx = x - halfWidthTarget
	
		
		if (y - halfWidthTarget < 0): 
			my = 0
		elif (y + widthTarget > resolutiony):	
			my = resolutiony - widthTarget
		else:
			my = y - halfWidthTarget	
		#print('x : ' + str(x) + " - " + " y : " + str(y))
		
# created a "threaded" video stream, allow the camera sensor to warmup
vs = PiVideoStream((resolutionx, resolutiony)).start()
time.sleep(1.0)

# Lecture de l'image
reticule = cv2.imread("target-red.png")
reticule = imutils.resize(reticule, width=widthTarget)
rows, cols, channels = reticule.shape


# Masks creation
grayreticule = cv2.cvtColor(reticule, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(grayreticule, 127, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Initialisation window
cv2.namedWindow('Target', cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback("Target", moveTarget)

# Loop over the frames of the video
while True :

	# grab the current frame
	frame = vs.read()
	
	frame2 = imutils.resize(frame, width=resolutionx)

	# ROI definition
	roi = frame2[my:rows+my, mx:cols+mx]
	
	#print('mx : ' + str(mx) + " - my : " + str(my) + " - rows : " +  str(rows+mx) + " - cols : " + str(cols+my))
	
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
			
	# wait user action
	key = cv2.waitKey(1) & 0xFF
		
	# if the 'q' key is pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
