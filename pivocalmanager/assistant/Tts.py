#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
import pyttsx
import logging

class Tts():
	
	""" Initilisation de la synthèse vocal """
	def __init__(self):
		self.logger = logging.getLogger(self.__class__.__name__)
		self.speech_engine = pyttsx.init('espeak')
		self.speech_engine.setProperty('voice',b'french')
		self.speech_engine.setProperty('rate',150)

	def speak(self, texte):
		self.speech_engine.say(texte)
		self.speech_engine.runAndWait()
		
	def listerVoix(self):
		self.logger.info('Liste des voix possibles : ')
		voices = speech_engine.getProperty('voices')
		for voice in voices:
			self.logger.info(voice.id)
			self.speech_engine.setProperty('voice',voice.id)
			self.speech_engine.say(text)
