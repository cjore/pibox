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
		self.listen = False
	
		
	""" Initialise et échantillonne le flux audio pour traitement """
	def initialiserMicro(self):
		self.logger.info('Initialisation du micro"')
		
		with speech_recognition.Microphone(device_index = 2, sample_rate = 48000, chunk_size = 1024) as source:
			self.recognizer.adjust_for_ambient_noise(source)
			self.audio = self.recognizer.listen(source)
		self.logger.info("Son détecté par la micro")
		
	"""	Initialise et échantillonne en tâche de fond le flux audio pour traitement """
	def initialiserMicroOffLine(self, keyword_entries):
		m = speech_recognition.Microphone(device_index = 2, sample_rate = 48000, chunk_size = 512)
		with m as source:
			self.recognizer.adjust_for_ambient_noise(source)
			self.logger.info("Flux audio en cours de traitement...")
			audio = self.recognizer.listen(source)
			stt = self.recognizer.recognize_sphinx(audio, "fr-FR", keyword_entries, False)
			self.logger.info(stt)
		return stt
		
	"""	Initialise et échantillonne en tâche de fond le flux audio pour traitement """
	def initialiserMicroInLine(self, keyword_entries):
		m = speech_recognition.Microphone(device_index = 2, sample_rate = 48000, chunk_size = 1024)
		with m as source:
			self.recognizer.adjust_for_ambient_noise(source)
			audio = self.recognizer.listen(source)
			self.logger.info("Flux audio en cours de traitement...")
			stt = self.recognizer.recognize_google(audio, None, "fr-FR", keyword_entries, False)
			self.logger.info(stt)
		return stt			
	
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
			stt = self.recognizer.recognize_google(audio, None, "fr-FR", keyword_entries, False)
			after = datetime.now()
			
			duree = after - before
			self.logger.info("Duree du recognizer google : {0}".format(duree))
			self.logger.info("Texte interprété par Sphinx : {0}".format(stt))
				
		except speech_recognition.UnknownValueError:
			self.logger.info("Could not understand audio")
		except speech_recognition.RequestError as e:
			self.logger.info("Recog Error; {0}".format(e))
						
		return stt
		
	
	""" Ecoute en tâche de fond """
	def listenOffLineInBackground(self,botOn,botOff,keyword_entries=None):
		print(self.listen)
		while self.listen == False:
			self.logger.info("En attente du bot...")
			try:
				stt = self.initialiserMicroOffLine(keyword_entries)
					
				try:
					if(botOn in stt.lower()):
						listen = True
						self.logger.info("En écoute...")
						break
					else:
						continue
				except LookupError:
					continue
			except speech_recognition.UnknownValueError:
				continue
				
		while self.listen == True:
			print("En attente de la commande...")
			try:
				stt = self.initialiserMicroOffLine(keyword_entries)
				
				if(stt.lower() == botOff):
					listen = False
					self.logger.info("Ecoute des commandes terminée.")
					break
				else:
					self.logger.info("Texte interprété par Sphinx : {0}".format(stt))
					return stt
			except LookupError:
				self.logger.info("Could not understand audio")
			except speech_recognition.UnknownValueError:
				self.logger.info("Google Speech Recognition could not understand audio")
				continue
			except speech_recognition.RequestError:
				self.logger.info("Could not request results from Google Speech Recognition service")
				continue			 				 			

	""" Ecoute en tâche de fond """
	def listenInLineInBackground(self,botOn, botOff, listen, keyword_entries=None):
		listen = False

		while True:
			while listen == False:
				self.logger.info("En attente du bot...")
				try:
					stt = self.initialiserMicroInLine(keyword_entries)
						
					try:
						if(botOn in stt.lower()):
							listen = True
							self.logger.info("En écoute...")
							break
						else:
							continue
					except LookupError:
						continue
				except speech_recognition.UnknownValueError:
					continue
					
			while listen == True:
				print("En attente de la commande...")
				try:
					stt = self.initialiserMicroInLine(keyword_entries)
					
					if(pinger.lower() == botOff):
						listen = False
						self.logger.info("Ecoute des commandes terminée.")
						break
					else:
						self.logger.info("Texte interprété par Google : {0}".format(stt))
						return stt
				except LookupError:
					self.logger.info("Could not understand audio")
				except speech_recognition.UnknownValueError:
					self.logger.info("Google Speech Recognition could not understand audio")
					continue
				except speech_recognition.RequestError:
					self.logger.info("Could not request results from Google Speech Recognition service")
					continue		
	
		
	


