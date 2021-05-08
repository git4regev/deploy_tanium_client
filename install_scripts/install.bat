@echo off
net session >nul 2>&1
if %errorlevel%==0 (
  goto Setup
) else (
  goto AdminErr
)
:Setup
@echo on
"%~dp0SetupClient.exe" /S
@echo off
if %errorlevel% ==0 (
  echo Setup complete.
) else (
  echo Setup failed.
)
copy "%~dp0tanium-init.dat" "c:\Program Files (x86)\Tanium\Tanium Client\tanium-init.dat"
goto Exit
:AdminErr
echo Install script must be run as administrator.
:Exit
pause
