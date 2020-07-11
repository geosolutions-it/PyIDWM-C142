REM This script is used to run coverage inside PyCharm Community Edition and using the Python environment of the project
SET PYTHON_EXE="./Scripts/python.exe"
%PYTHON_EXE% -m coverage run -m unittest discover 
%PYTHON_EXE% -m coverage report --omit=*/__init__.py
%PYTHON_EXE% -m coverage html --omit=*/__init__.py