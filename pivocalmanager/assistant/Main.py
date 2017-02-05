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
from CsvUtils import CsvUtils

class Main():
	
	# Constructeur
	def __init__(self):
		self.stt = Stt()
		self.tts = Tts()
		self.traitementCommandeVocale = TraitementCommandeVocale()
		self.lancerAssistant()
		
	def lancerAssistant(self):
		#Chargement des mots reconnu par le programme
		keywords = CsvUtils.transformerCsvEnListeKeyword('Keywords.csv');
		print(keywords)
		#Transformation de la parole en texte
		commande = self.stt.listenOffLine(keywords)
		
		#Interprétation textuelle de la commande	
		reponse = self.traitementCommandeVocale.do(commande)
		
		#Génération de la synthèse vocale 
		self.tts.speak(reponse)
		
if __name__ == "__main__":
	Main()

