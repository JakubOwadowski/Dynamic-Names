#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Setup complete. Run with: source venv/bin/activate && ./main.py"