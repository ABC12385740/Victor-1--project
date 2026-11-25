@echo off
REM Victor (202384014045)
REM Start the Tetris game from the top of this folder, so Ctrl+Shift+B works
REM no matter whether VS Code opened "Victor_202384014045" or "tetris-game".
setlocal
cd /d "%~dp0tetris-game"
if not exist "run.bat" (
    echo run.bat not found in tetris-game\
    pause
    exit /b 1
)
call run.bat
