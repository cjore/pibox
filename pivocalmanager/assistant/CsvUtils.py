#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv

class CsvUtils():
	
	@staticmethod
	def transformerCsvEnListe(filename):
		csvEnListe = []
		with open(filename,'rt') as f:
			csvreader = csv.reader(f, delimiter=';')
		
			for row in csvreader:
				
				taille = len(row)
				ligne = "("
				for i in range(0, taille):
					if (i == taille - 1):
						ligne = ligne + row[i]
					else:	
						ligne = ligne + row[i] + ","
				ligne = ligne + ")"
				csvEnListe.append(ligne)
	
		return csvEnListe
		
	@staticmethod
	def transformerCsvEnListeKeyword(filename):		
		keywords = []
		with open(filename,'rt') as f:
			csvreader = csv.reader(f, delimiter=';')
		
			for row in csvreader:
				keyword = (str(row[0]), int(row[1]))
				keywords.append(keyword)
				
		return keywords
