#!/bin/bash

echo "Installing python-pip"
sudo pacman -S python-pip 
source .venv/bin/activate
echo "Installing Requirements"
pip install -r requirements.txt
python install.py
