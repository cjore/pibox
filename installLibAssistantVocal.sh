#!/usr/bin/env bash

#pyaudio 0.2.9
sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip3install pyaudio
sudo pip3install pyaudio --upgrade

#pocketsphinx
sudo apt-get install python3 python3-all-dev python3-pip build-essential swig git libpulse-dev
sudo pip3 install pocketsphinx

#flac
sudo apt-get install flac

#SpeechRecognition
sudo pip3 install SpeechRecognition

#Langue Francaise	
SR_LIB=$(python3 -c "import speech_recognition as sr, os.path as p; print(p.dirname(sr.__file__))")
sudo apt-get install --yes wget unzip
sudo wget https://www.dropbox.com/s/115e3mf3y21x0b8/fr-FR.zip?dl=1 -O "$SR_LIB/fr-FR.zip"
sudo unzip -o "$SR_LIB/fr-FR.zip" -d "$SR_LIB"
sudo chmod --recursive a+r "$SR_LIB/fr-FR/"

#Pyttsx
sudo wget https://github.com/jpercent/pyttsx/archive/master.zip
sudo unzip master.zip
cd pyttsx-master
sudo python3 setup.py install --user
cd dist
sudo easy_install3 pyttsx-1.2-py3.4.egg
