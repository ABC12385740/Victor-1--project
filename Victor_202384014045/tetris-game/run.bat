@echo off
REM Double-click this file on Windows to play: it starts Flask and opens the page.
REM Victor (202384014045)
setlocal
cd /d "%~dp0"

REM Find a Python interpreter: PATH first, then the launcher, then common folders.
set "PY="
python --version >nul 2>nul
if not errorlevel 1 set "PY=python"
if defined PY goto :found

py -3 --version >nul 2>nul
if not errorlevel 1 set "PY=py -3"
if defined PY goto :found

for %%D in ("%LOCALAPPDATA%\Programs\Python\Python3*" "C:\Python3*" "D:\Python3*" "%ProgramFiles%\Python3*") do (
    if not defined PY if exist "%%~fD\python.exe" set "PY=%%~fD\python.exe"
)
if defined PY goto :found

echo Python was not found on this computer.
echo Install Python 3.10 or newer from https://www.python.org/downloads/
echo and tick "Add python.exe to PATH", then run this file again.
pause
exit /b 1

:found
echo Using %PY%

%PY% -c "import flask" >nul 2>nul
if errorlevel 1 (
    echo Installing Flask, this only happens once...
    %PY% -m pip install -r requirements.txt
)

netstat -ano | findstr /C:"127.0.0.1:5000" | findstr /C:"LISTENING" >nul
if errorlevel 1 goto :startserver
echo The server is already running on port 5000.
goto :open

:startserver
echo Starting the server at http://127.0.0.1:5000
start "Tetris server" /min cmd /c "%PY% app.py"
timeout /t 3 /nobreak >nul

:open
start "" "http://127.0.0.1:5000"
echo The game should be open in your browser.
echo To stop it, close the minimised "Tetris server" window.
