@echo off

net file 1>NUL 2>NUL
if not '%errorlevel%' == '0' (
    powershell Start-Process -FilePath "%0" -ArgumentList "%cd%" -verb runas >NUL 2>&1
    exit /b
)

:: Change directory with passed argument. Processes started with
:: "runas" start with forced C:\Windows\System32 workdir
cd /d %1

REM Be sure to change this to the drive letter you want to mount the drive to!
set drive=D

REM Be sure to change this to the Volume Name of the drive you want to mount!
set volume=\\?\Volume{9b19555f-d1b0-49c5-bc40-9910d3d41c55}\

:start
echo Mounting Drive...
mountvol %drive%: %volume%
echo Drive Mounted!
exit