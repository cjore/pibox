#!/usr/bin/python3
# -*- coding: utf-8 -*-

from espeak import espeak
#import espeak
import subprocess

text = '"Safe mode!"'
subprocess.call('espeak -v fr+m6 '+text, shell=True)
subprocess.call('espeak '+text, shell=True)

#espeak.list_voices()
espeak.set_voice('fr')
espeak.synth("Hello Instructables!")

#def voices = espeak.list_voices()
#for voice in voices :
#	print voice
