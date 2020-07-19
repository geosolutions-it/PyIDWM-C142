#!/bin/bash
#This script is used to run coverage inside PyCharm Community Edition and using the Python environment of the project
python -m coverage run -m unittest discover 
python -m coverage report --omit=*/__init__.py
python -m coverage html --omit=*/__init__.py