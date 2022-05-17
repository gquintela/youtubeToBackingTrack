#!/bin/bash

source venv/bin/activate

if [ $# -eq 1 ]; then
  python3 main.py $1
else
  python3 main.py
fi

deactivate