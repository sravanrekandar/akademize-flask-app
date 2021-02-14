#!/bin/bash
export FLASK_ENV=development
export FLASK_APP=src/app.py

python -m venv .venv
source .venv/bin/activate

python -m pipenv run flask run
