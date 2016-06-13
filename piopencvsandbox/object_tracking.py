#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2
from imutils.video.pivideostream import PiVideoStream
import time

def run_main():
	# created a "threaded" video stream, allow the camera sensor to warmup
	vs = PiVideoStream((640,480)).start()
	time.sleep(2.0)
	
	# read the first frame of the video
	frame = vs.read()
	
	# Set the ROI
	c, r, w, h=200, 100, 70, 70
	track_window=(c, r, w, h)
	
	# Create mask and nomralized histogram
	roi = frame[r:r+h, c:c+w]
	hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv_roi, np.array((0., 30., 32.)), np.array((180.,255.,255.)))
	roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
	cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
	
	# Setup the termination criteria, either 80 iteration or move by atleast 1pt
	term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 80, 1)
	
	while True:
		frame = vs.read()
	
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
		
		# apply meanshift to get the new location
		ret, track_window = cv2.meanShift(dst, track_window, term_crit)
		
		# apply camshift to get the new location
		#ret, track_window = cv2.CamShift(dst, track_window, term_crit)

		# draw it on image
		x, y, w, h = track_window
		cv2.rectangle(frame, (x, y), (x+w, y+h), 255, 2)
		cv2.putText(frame, 'Tracked M', (x-25, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
		
		cv2.imshow('Tracking', frame)
		
		# if the 'q' key is pressed, break from the loop
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			break
			
	vs.stop()
	cv2.destroyAllWindows()
	
if __name__ == "__main__":
	run_main()	
