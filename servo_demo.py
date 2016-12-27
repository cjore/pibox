#!/usr/bin/python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

servo_pin=12 #equivalent de GPIO 18

depart = 3 #rapport cyclique pour que le servo soit au début de son mouvement

arrivee = 13 #rapport cyclique pour que le servo soit à la fin de son mouvement

GPIO.setmode(GPIO.BOARD) #notation board plutôt que BCM
GPIO.setup(servo_pin, GPIO.OUT) #pin configurée en sortie

pwm = GPIO.PWM(servo_pin, 50) #pwm à une fréquence de 50 Hz

position = depart

pwm.start(depart)

while True:
	if position < arrivee :
		pwm.ChangeDutyCycle(float(position))
		position = position + 0.1
		time.sleep(0.1)
	else:
		position = depart
		
pwm.stop		

# valeur min 3 valeur max 13
