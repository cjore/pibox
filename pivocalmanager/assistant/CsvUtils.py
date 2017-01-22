#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv

class CsvUtils():
	
	@staticmethod
	def transformerCsvEnTuple(filename):
		cr = csv.reader(open(filename,"rb"))
		


