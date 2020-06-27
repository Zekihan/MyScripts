@echo off
cd C:\Coding\scrcpy-win64-v1.12.1

@echo off
CScript //nologo //E:JScript "%~F0" | .\scrcpy -s9befcc160904 -b16M -m2160 --window-x 1180 --window-width 420 --window-height 830 -S
if ERRORLEVEL 1 goto NORMAL
REM /B to avoid the command line window to close
EXIT /B %errorlevel%

:NORMAL	
.\adb connect 192.168.1.199:5555
.\scrcpy -b16M -m2160 --window-x 1180 --window-width 420 --window-height 830 -S

