@echo off
:: Put the lines below in a file in your local startup folder
:: Make a shortcut from C:\startup\profile_win_local.bat and place the shortcut here-
:: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup

setx SERVER <YOUR PATH TO MAIN SERVER>
setx PYTHONPATH %PYTHONPATH%;%SERVER%\SYSTEMS\python
call %SERVER%\SYSTEMS\startup\profile_win_global.bat