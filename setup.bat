@echo off
REM Healthcare System Setup Script for Windows

echo.
echo ========================================
echo AI-Powered Healthcare System Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/5] Checking Python version...
python --version

echo.
echo [2/5] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo.
echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [4/5] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [5/5] Setup complete!
echo.
echo ========================================
echo Setup Successful!
echo ========================================
echo.
echo To run the application, use:
echo   run.bat
echo.
echo Or manually run:
echo   venv\Scripts\activate
echo   streamlit run app.py
echo.
pause
