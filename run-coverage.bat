SET PYTHON_EXE="./Scripts/python.exe"
%PYTHON_EXE% -m coverage run -m unittest discover 
%PYTHON_EXE% -m coverage report --omit=*/__init__.py
%PYTHON_EXE% -m coverage html --omit=*/__init__.py