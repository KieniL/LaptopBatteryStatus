@echo on
REM Path to PythonDirectory
set PythonPath=C:\Users\U11643\Desktop\batterystatus
set VAR6=\Scripts\pip.exe
set VAR7=%PythonPath%%VAR6%
set VAR8=%PythonPath%\Scripts\python.exe

REM Update pip
"%VAR8%" -m pip install --upgrade pip


REM Use Python Interpreter to install python packages
"%VAR7%" install pywin32

