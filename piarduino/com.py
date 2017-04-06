#!/usr/bin/python3
# -*- coding: utf-8 -*-

import serial

ser = serial.Serial("/dev/ttyACM0", timeout=1)
print(ser)
while 1:
	code=input("Code à envoyer à l'Arduino: ")
	ser.write(code.encode('utf-8'))
	#ser.write(code)
