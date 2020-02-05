@echo off


set PythonPath=C:\Users\LukasKienast\AppData\Local\Programs\Python\Python37
set VAR7=\python.exe
set VAR8=%PythonPath%%VAR7%

REM Use Python Interpreter run python program and pass all variables to it
"%VAR8%" main.py
pause