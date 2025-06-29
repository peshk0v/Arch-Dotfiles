#!/bin/bash

echo "Installing python-pip"
sudo pacman -S python-pip 
python -m venv .venv
source .venv/bin/activate
echo "Installing Requirements"
pip install -r requirements.txt
python build.py
