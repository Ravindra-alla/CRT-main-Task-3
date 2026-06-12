#!/bin/bash
# Healthcare System Run Script

echo "Starting AI-Powered Healthcare System..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Running setup first..."
    bash setup.sh
fi

# Activate virtual environment
source venv/bin/activate

# Run the Streamlit app
echo ""
echo "========================================"
echo "Launching Healthcare System"
echo "========================================"
echo ""
echo "The application will open in your browser at:"
echo "http://localhost:8501"
echo ""
echo "Press CTRL+C to stop the server"
echo ""

streamlit run app.py --logger.level=info
