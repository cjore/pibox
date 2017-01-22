#!/usr/bin/python3
# -*- coding: utf-8 -*-

import speech_recognition
from datetime import datetime

class Stt():
	
	""" Initilisation de la reconnaissence vocal """
	def __init__(self):
		self.recognizer = speech_recognition.Recognizer()
	
		
	""" Initialise et échnatillonne le flux audio pour traitement """
	def initialiserMicro(self):
		print("Initialisation micro")
		with speech_recognition.Microphone(device_index = 2, sample_rate = 48000, chunk_size = 1024) as source:
			self.recognizer.adjust_for_ambient_noise(source)
			self.audio = self.recognizer.listen(source)
		print("Son détecté par la micro")	
	
	""" Ecoute d'une commande vocale avec Sphinx """
	def listenOffLine(self,keyword_entries=None):
		print("Listen Off Line...")
		self.initialiserMicro()
						
		before = datetime.now()
		print("Commande en cours de traitement : {0}".format(before))
			
		#speak("Commande en cours de traitement")
		stt=""	
		
		try:
				
			#Shpinx recognizer
			before = datetime.now()
			stt = self.recognizer.recognize_sphinx(self.audio, "fr-FR", keyword_entries, False)
			after = datetime.now()
			
			duree = after - before
			print("Duree du recognizer sphinx : {0}".format(duree))
			print(stt)
				
		except speech_recognition.UnknownValueError:
			print("Could not understand audio")
		except speech_recognition.RequestError as e:
			print("Recog Error; {0}".format(e))
						
		return stt
	
	""" Ecoute d'une commande vocale avec Google """
	def listenInLine(self,keyword_entries=None):
		print("Listen In Line...")
		self.initialiserMicro()
						
		before = datetime.now()
		print("Commande en cours de traitement : {0}".format(before))
			
		#speak("Commande en cours de traitement")
		stt=""	
		
		try:
				
			#Google recognizer
			before = datetime.now()
			stt = self.recognizer.recognize_sphinx(self.audio, None, "fr-FR", keyword_entries, False)
			after = datetime.now()
			
			duree = after - before
			print("Duree du recognizer google : {0}".format(duree))
			print(stt)
				
		except speech_recognition.UnknownValueError:
			print("Could not understand audio")
		except speech_recognition.RequestError as e:
			print("Recog Error; {0}".format(e))
						
		return stt
	
		
	


