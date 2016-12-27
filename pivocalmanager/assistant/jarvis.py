#!/usr/bin/python3
# -*- coding: utf-8 -*-

import speech_recognition
from datetime import datetime

recognizer = speech_recognition.Recognizer()

def listen():
	with speech_recognition.Microphone(device_index = 2, sample_rate = 44100, chunk_size = 512) as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
		
	try:
		before = datetime.now()
		print("Before recognizer : {0}".format(before))
				
		stt = recognizer.recognize_sphinx(audio, "fr-FR")
		
		after = datetime.now()
		print("After recognizer : {0}".format(after)) 
		
		duree = after - before
		print("Duree du traitement : {0}".format(duree))
		
		return stt
		
	except 	speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except 	speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))
		
	return ""			
	
print(listen())	
	
