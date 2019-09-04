@echo off


set PythonPath=C:\Users\U11643\Desktop\batterystatus
set var6=\Scripts\
set VAR7=%VAR6%python.exe
set VAR8=%PythonPath%%VAR7%

REM Use Python Interpreter run python program and pass all variables to it
"%VAR8%" main.py
pause