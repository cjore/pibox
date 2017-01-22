#!/usr/bin/python3
# -*- coding: utf-8 -*-

class TraitementCommandeVocale():
	
	def __init__(self):
		print("Traitement")
	
	# Analyse de la commande vocal et dispatch des actions 
	def do(self, text):
		
		cmd = text.lower()
		
		if (cmd=="bonjour"):
			return "Bonjour"
		else:
			if ("lancer" in cmd):
				if ("programme un" in cmd):
					return "programme un lancé"
				if ("programme deux" in cmd):
					return "programme deux lancé"	 
			else:	
				return "Veuillez reformulez!"	
