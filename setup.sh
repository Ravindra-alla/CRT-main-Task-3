#!/bin/bash
# Healthcare System Setup Script for Linux/Mac

echo ""
echo "========================================"
echo "AI-Powered Healthcare System Setup"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

echo "[1/5] Checking Python version..."
python3 --version

echo ""
echo "[2/5] Creating virtual environment..."
python3 -m venv venv

echo ""
echo "[3/5] Activating virtual environment..."
source venv/bin/activate

echo ""
echo "[4/5] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "[5/5] Setup complete!"
echo ""
echo "========================================"
echo "Setup Successful!"
echo "========================================"
echo ""
echo "To run the application, use:"
echo "  ./run.sh"
echo ""
echo "Or manually run:"
echo "  source venv/bin/activate"
echo "  streamlit run app.py"
echo ""
