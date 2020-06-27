@echo off

net file 1>NUL 2>NUL
if not '%errorlevel%' == '0' (
    powershell Start-Process -FilePath "%0" -ArgumentList "%cd%" -verb runas >NUL 2>&1
    exit /b
)

:: Change directory with passed argument. Processes started with
:: "runas" start with forced C:\Windows\System32 workdir
cd /d %1

REM Be sure to change this to the drive you want to unmount! 
set drive=D:

echo Unmounting Drive...
mountvol %drive% /p
echo Drive Unmounted!

exit