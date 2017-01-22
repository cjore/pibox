#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
import pyttsx

class Tts():
	
	""" Initilisation de la synthèse vocal """
	def __init__(self):
		self.speech_engine = pyttsx.init('espeak')
		self.speech_engine.setProperty('voice',b'french')
		self.speech_engine.setProperty('rate',150)

	def speak(self, texte):
		self.speech_engine.say(texte)
		self.speech_engine.runAndWait()
		
	def listerVoix(self):
		voices = speech_engine.getProperty('voices')
		for voice in voices:
			print(voice.id)
			self.speech_engine.setProperty('voice',voice.id)
			self.speech_engine.say(text)
