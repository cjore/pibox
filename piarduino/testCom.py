#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Le raspberry pi  demande une information à l'arduino,
# puis il affiche la réponse à l'écran

import serial 
import time

ser = serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=1)
time.sleep(4) # on attend un peu pour que l'arduino soit prêt

while True:
	ser.write('5'.encode('utf-8'))
	reponse = ser.readline()
	print(reponse) # on affiche la réponse
	if (reponse.decode("utf-8") == "test"):
		print("OK")
	time.sleep(1)
