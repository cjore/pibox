#!/usr/bin/python3
# -*- coding: utf-8 -*-

import speech_recognition
from datetime import datetime
import logging

class Stt():
	
	""" Initilisation de la reconnaissence vocal """
	def __init__(self):
		self.recognizer = speech_recognition.Recognizer()
		self.logger = logging.getLogger(self.__class__.__name__)
	
		
	""" Initialise et échnatillonne le flux audio pour traitement """
	def initialiserMicro(self):
		self.logger.info('Initialisation du micro"')
		
		with speech_recognition.Microphone(device_index = 2, sample_rate = 48000, chunk_size = 1024) as source:
			self.recognizer.adjust_for_ambient_noise(source)
			self.audio = self.recognizer.listen(source)
		self.logger.info("Son détecté par la micro")	
	
	""" Ecoute d'une commande vocale avec Sphinx """
	def listenOffLine(self,keyword_entries=None):
		self.logger.info("Listen Off Line...")
		self.initialiserMicro()
						
		before = datetime.now()
		self.logger.info("Commande en cours de traitement : {0}".format(before))
			
		#speak("Commande en cours de traitement")
		stt=""	
		
		try:
				
			#Shpinx recognizer
			before = datetime.now()
			stt = self.recognizer.recognize_sphinx(self.audio, "fr-FR", keyword_entries, False)
			after = datetime.now()
			
			duree = after - before
			self.logger.info("Duree du recognizer sphinx : {0}".format(duree))
			self.logger.info("Texte interprété par Sphinx : {0}".format(stt))
				
		except speech_recognition.UnknownValueError:
			self.logger.info("Could not understand audio")
		except speech_recognition.RequestError as e:
			self.logger.info("Recog Error; {0}".format(e))
						
		return stt
	
	""" Ecoute d'une commande vocale avec Google """
	def listenInLine(self,keyword_entries=None):
		self.logger.info("Listen In Line...")
		self.initialiserMicro()
						
		before = datetime.now()
		self.logger.info("Commande en cours de traitement : {0}".format(before))
			
		#speak("Commande en cours de traitement")
		stt=""	
		
		try:
				
			#Google recognizer
			before = datetime.now()
			stt = self.recognizer.recognize_sphinx(self.audio, None, "fr-FR", keyword_entries, False)
			after = datetime.now()
			
			duree = after - before
			self.logger.info("Duree du recognizer google : {0}".format(duree))
			self.logger.info("Texte interprété par Sphinx : {0}".format(stt))
				
		except speech_recognition.UnknownValueError:
			self.logger.info("Could not understand audio")
		except speech_recognition.RequestError as e:
			self.logger.info("Recog Error; {0}".format(e))
						
		return stt
	
		
	


