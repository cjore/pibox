#!/usr/bin/python3
# -*- coding: utf-8 -*-

import serial
import time
from time import sleep

ser = serial.Serial("/dev/ttyACM0", timeout=1)
time.sleep(4) # on attend un peu pour que l'arduino soit prêt
print(ser)

def do():
	return "263"
	
def re():
	return "293"
	
def mi():		
	return "329"
	
def fa():		
	return "349"

def sol():		
	return "392"

def la():		
	return "440"
	
def si():		
	return "493"

def nul():
	return "0"
	
def hymne(sequence):
	for note in sequence:
		freq = note()
		print("note : {} - frequence : {}".format(note,freq))
		ser.write(freq.encode('utf-8'))
		reponse = ser.readline()
		print(reponse)
		while reponse.decode("utf-8") != "OK\r\n":
			print("boucle")
			reponse = ser.readline()
			print(reponse)
		 
notes = {7:do,
	8:re,
	9:mi,
	4:fa,
	5:sol,
	6:la,
	1:si,	
}

#while 1:
#	code=input("Code à envoyer à l'Arduino: ")
	 
#	freq = notes[int(code)]() 
#	ser.write(freq.encode('utf-8'))
	#ser.write(code)

hymne([si,si,do,re,re,do,si,la,sol,sol,la,si,si,nul,nul,la,nul,nul])
#hymne([si,si,do,re,re,do,si,la,sol,sol,la,si,la,nul,nul,sol,nul,nul])	
#hymne([la,la,si,sol,la,si,do,si,sol,la,si,do,si,la,sol,la,re,nul,si])		
#hymne([si,do,re,re,do,si,la,sol,sol,la,si,la,nul,nul,sol,sol,nul,nul])	
