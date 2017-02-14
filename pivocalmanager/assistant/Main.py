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
import logging
import logging.config

class Main():
	
	# Constructeur
	def __init__(self):
		#Initialisation du logger
		logging.config.fileConfig('logging.conf')
		self.logger = logging.getLogger(self.__class__.__name__)
		
		self.logger.info('Initialisation du programme')
		
		self.stt = Stt()
		self.tts = Tts()
		self.traitementCommandeVocale = TraitementCommandeVocale()
		self.lancerAssistant()
				
	def lancerAssistant(self):
		#Chargement des mots reconnu par le programme
		keywords = CsvUtils.transformerCsvEnListeKeyword('Keywords.csv');
		self.logger.info('Chargement du dictionnaire réduit : {0}'.format(keywords))
				
		#Transformation de la parole en texte
		commande = self.stt.listenOffLine(keywords)
		
		#Interprétation textuelle de la commande	
		reponse = self.traitementCommandeVocale.do(commande)
		self.logger.info('Commande interprété par le programme : {0}'.format(reponse))
		
		#Génération de la synthèse vocale 
		self.tts.speak(reponse)
			
			
		
if __name__ == "__main__":
	Main()

