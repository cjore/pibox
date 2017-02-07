#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

class TraitementCommandeVocale():
	
	def __init__(self):
		self.logger = logging.getLogger(self.__class__.__name__)
	
	# Analyse de la commande vocale et dispatch des actions 
	def do(self, text):
		self.logger.info("Traitement commande vocale en cours ...")
		cmd = text.lower()
		
		if ("bonjour" in cmd):
			return "Bonjour"
		else:
			if ("lancer" in cmd):
				if ("programme un" in cmd):
					return "programme un lancé"
				if ("programme deux" in cmd):
					return "programme deux lancé" 
			else:	
				return "Veuillez reformulez!"	
