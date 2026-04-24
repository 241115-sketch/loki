@echo off
title L.O.K.I — REY XXXVII Launcher
echo ======================================================
echo    L.O.K.I: Logical Operational Kinetic Intelligence
echo ======================================================
echo.

:: Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3.11+ from python.org
    pause
    exit /b
)

echo [1/3] Checking requirements...
pip install -r requirements.txt --quiet

echo [2/3] Setting up browsers...
python -m playwright install chromium --quiet

echo [3/3] Initializing L.O.K.I...
echo.
echo Launching HUD...
python main.py

pause
