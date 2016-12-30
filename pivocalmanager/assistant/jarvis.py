#!/usr/bin/python3
# -*- coding: utf-8 -*-

import speech_recognition
from datetime import datetime
import pyttsx

speech_engine = pyttsx.init('espeak')
speech_engine.setProperty('voice',b'french')
speech_engine.setProperty('rate',150)

def speak(text):
		
	#voices = speech_engine.getProperty('voices')
	#for voice in voices:
	#	print(voice.id)
	#	speech_engine.setProperty('voice',voice.id)
	#	speech_engine.say(text)
	
	speech_engine.say(text)
	speech_engine.runAndWait() 


recognizer = speech_recognition.Recognizer()

def listen():
	with speech_recognition.Microphone(device_index = 2, sample_rate = 44100, chunk_size = 512) as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
		
	try:
		before = datetime.now()
		print("Before recognizer : {0}".format(before))
		
		speak("Commande en cours de traitement")
				
		#stt = recognizer.recognize_sphinx(audio, "fr-FR", [('bonjour',1)], False)
		stt = recognizer.recognize_sphinx(audio, "fr-FR")
		
		after = datetime.now()
		print("After recognizer : {0}".format(after)) 
		
		duree = after - before
		print("Duree du recognizer : {0}".format(duree))
		
		return stt
		
	except 	speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except 	speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))
		
	return ""			

def do(text):
	if (text=="bonjour"):
		return "Bonjour"
	else:
		return "Veuillez reformulez!"	

commande = listen()
print(commande)	
reponse = do(commande)
speak(reponse)
	
