#!/usr/bin/python3
# -*- coding: utf-8 -*-

import speech_recognition as sr

r = sr.Recognizer()

listen = False

while True:
	while listen == False:
		try:
			m = sr.Microphone(device_index = 2, sample_rate = 48000, chunk_size = 1024)
			with m as source:
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
				print("pinger")
				#pinger = r.recognize_google(audio)
				pinger = r.recognize_sphinx(audio, "fr-FR", [('bonjour',1)], False)
				
			try:
				print(pinger)
				if(pinger.lower() == "start"):
					listen = True
					print("Listening...")
					break
				else:
					continue
			except LookupError:
				continue
		except sr.UnknownValueError:
			continue
			
	while listen == True:
		print("2nd part")
		try:
			m = sr.Microphone(device_index = 2, sample_rate = 48000, chunk_size = 1024)
			with m as source:
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
				#pinger = r.recognize_google(audio)
				pinger = r.recognize_sphinx(audio, "fr-FR", [('bonjour',1)], False)
			print("1")
			
			print("2")
			if(pinger.lower() == "stop"):
				listen = False
				print("Listening stopped.")
				break
			else:
					print("You said " + pinger)
		except LookupError:
			print("Could not understand audio")
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
			continue
		except sr.RequestError:
			print("Could not request results from Google Speech Recognition service")
			continue			 				 			
