@echo off
REM Healthcare System Run Script

echo Starting AI-Powered Healthcare System...
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Virtual environment not found. Running setup first...
    call setup.bat
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run the Streamlit app
echo.
echo ========================================
echo Launching Healthcare System
echo ========================================
echo.
echo The application will open in your browser at:
echo http://localhost:8501
echo.
echo Press CTRL+C to stop the server
echo.

streamlit run app.py --logger.level=info

pause
