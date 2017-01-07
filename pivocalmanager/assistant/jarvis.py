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
	with speech_recognition.Microphone(device_index = 2, sample_rate = 48000, chunk_size = 1024) as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
		
		
	before = datetime.now()
	print("Commande en cours de traitement : {0}".format(before))
		
	speak("Commande en cours de traitement")
	stt=""	
	
	try:
			
		#Shpinx avec keyword entrie
		before = datetime.now()
		stt = recognizer.recognize_sphinx(audio, "fr-FR", [('bonjour',1)], False)
		after = datetime.now()
		
		duree = after - before
		print("Duree du recognizer sphinx avec keyword : {0}".format(duree))
		print(stt)
			
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))
		
	
	try:
		#Sphinx
		before = datetime.now()
		stt = recognizer.recognize_sphinx(audio, "fr-FR")
		after = datetime.now()
		
		duree = after - before
		print("Duree du recognizer sphinx : {0}".format(duree))
		print(stt)
		
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))	
		
	try:	
		#Google
		before = datetime.now()
		stt = recognizer.recognize_google(audio, None, "fr-FR")
		after = datetime.now()
		
		duree = after - before
		print("Duree du recognizer google : {0}".format(duree))
		print(stt)
		
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))
		
	return stt
		

def do(text):
	
	if (text=="bonjour"):
		return "Bonjour"
	else:
		return "Veuillez reformulez!"	

commande = listen()
print(commande)	
reponse = do(commande)
speak(reponse)
