#!/usr/bin/env bash
 
# Set start time so we know how long the bootstrap takes
 
T="$(date +%s)"
 
#echo 'Updating'
 
sudo apt-get -y update

sudo apt-get -y install python-pip libffi-dev libssl-dev python3-pip libjpeg-dev zlib1g-dev libpng-dev python-xlib python-tk python-dev build-essential

easy_install -U pip

sudo -H pip install --upgrade pyopenssl ndg-httpsclient pyasn1 pip requests pyopenssl ndg-httpsclient pyasn1 setuptools ez_setup Image Pillow python-xlib pyautogui selenium

sudo -H easy_install -U setuptools
