@echo off
set /p port_id=Please input the port id that you want to end with:
python killProcess.py -p %port_id%
pause>nul