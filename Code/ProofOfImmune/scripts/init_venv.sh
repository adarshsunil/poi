#!/bin/sh

# Source this file with . ./scripts/init_env.sh
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt