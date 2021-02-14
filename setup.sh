#!/bin/bash
echo "Akademize Flask App project setup script"
echo "----------------------------------"

python --version
python -m pip --version
python -m pip install --upgrade pip

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install Pipenv
python -m pip install pipenv

# Install dependencies
# python -m pipenv install -r requirements.txt
