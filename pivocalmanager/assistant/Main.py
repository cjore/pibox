#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
import Stt
import Tts
import TraitementCommandeVocale
"""
from Stt import Stt
from Tts import Tts
from TraitementCommandeVocale import TraitementCommandeVocale

class Main():
	
	# Constructeur
	def __init__(self):
		self.stt = Stt()
		self.tts = Tts()
		self.traitementCommandeVocale = TraitementCommandeVocale()
		self.lancerAssistant()
		
	def lancerAssistant(self):
		#Transformation de la parole en texte
		commande = self.stt.listenOffLine()
		
		#Interprétation textuelle de la commande	
		reponse = self.traitementCommandeVocale.do(commande)
		
		#Génération de la synthèse vocale 
		self.tts.speak(reponse)
	
if __name__ == "__main__":
	Main()

