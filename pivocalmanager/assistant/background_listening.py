#!/usr/bin/python3
# -*- coding: utf-8 -*-

import speech_recognition as sr

# this is called from the bacground thread
def callback(recognizer, audio):
	print('callback') 
	#received audio data, now we'll recognize it using Google Speech Recognition
	try:
		print("Google speech recognition thinks you said " + recognizer.recognize_google(audio))
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
		
r = sr.Recognizer()
m = sr.Microphone(device_index = 2, sample_rate = 48000, chunk_size = 1024)

with m as source:
	r.adjust_for_ambient_noise(source)

# start listening in the background	
stop_listening = r.listen_in_background(m, callback)			 
# stop_listening is now a function that, when called, stop background listening

# do some other computation for 5 seconds, then stop listening and keep doing other computations
import time
for _ in range(50): time.sleep(0.1) # we're still listening even though the main thread is doing other things
stop_listening() # calling this function requests that the background listener stop listening
while True: time.sleep(0.1) 
